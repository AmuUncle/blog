---
title: 第16节 MFC之SendMessage和PostMessage
date: 2017-11-04 23:33:16
tags:
---

> 1、**PostMessage**会将消息压入窗口所在线程的消息队列，然后返回；而SendMessage则不经过消息队列，**SendMessage**可认为是直接调用了该窗口的窗口过程，因此在我们需要获得消息处理后的返回值的时候，就要用到**SendMessage**。
>     例如：当在程序中指定如下使用：**PostMessage（hWnd, WM_MSG,0,0）**，那么当程序执行到PostMessage的时候，仅将消息WM_MSG压入到创建hWnd所指窗口的那个线程的消息队列，然后程序将继续执行下去，而至于程序什么时候响应该消息，则要看那个线程什么时候得到控制权；
>     而指定如下使用：**SendMessage（hWnd, WM_MSG,0,0）**，那么当程序执行到该处时，将发生一次跳转：从当前位置，跳转到hWnd的窗口过程中去响应WM_MSG消息，当消息处理结束，窗口过程返回，程序又将从**SendMessage**后面继续执行，当然，我们可以获得窗口过程对该消息的处理结果，也即取**SendMessage**的返回值。（这里只是针对单线程）。

> 2、在多线程应用中，**PostMessage**的用法还是一样，但**SendMessage**则不同了。如果在线程A中向线程B所创建的一个窗口hWndB发送消息**SendMessage（hWndB，WM_MSG，0，0）**，那么系统将会立即将执行权从线程A切换到线程B，然后在线程B中调用hWndB的窗口过程来处理消息，并且在处理完该消息后，执行权仍然在B手中！这个时候，线程A则暂停在**SendMessage**处，等待下次线程A获得执行权后才继续执行，并且仍然可以获得消息处理的结果（返回值）。一般，为了避免死锁，在B中对WM_MSG做出处理之前，要加上：
> if(InSendMessage()) RelpyMessage(lResult)； 即判断：如果该消息是发自另外一个线程，则立即 RelpyMessage，回复消息，参数lResult即是返回值。而如果是在同一个线程内，则InSendMessage()将会返回FALSE。     ---百度知道

总而言之，按我的理解，**SendMessage**和**PostMessage**都是向窗体发送消息的函数，但是**PostMessage**发送完消息立刻返回，不会等待消息结果，但**SendMessage**会等到消息返回结果再执行下一步；

今天我们通过各例子来试试这两种发送消息的方法；

> 创建一个界面图标，通过拖动图标到任意的windows窗口上，获取到窗口的句柄，标题，类名；并通过**SendMessage**或**PostMessage**发送消息到该窗口，修改窗口标题或关闭窗口；

## 1. 新建项目
新建一个基于对话框项目“day18”，布局如下，自行处理： 
![这里写图片描述](http://img.blog.csdn.net/20171104224025288?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 2. 新建类Cday18Dlg成员变量

```
	HCURSOR m_hCursor;  //定义一个鼠标的指针
	RECT m_rtCtrl;      //图标的大小
	BOOL m_bCapturing;   //鼠标捕获
	HWND m_hWndDest;   //目标窗口的窗口句柄
```

## 3.加载鼠标指针及获取图标大小
编辑Cday18Dlg::OnInitDialog()初始化函数，在return之前添加如下两行

```
	m_hCursor = LoadCursor(NULL, IDC_SIZEALL);
	GetDlgItem(IDC_PIC)->GetWindowRect(&m_rtCtrl);
```
## 4.创建鼠标右键点击及释放消息
如图，添加OnLButtonDown及OnLButtonUp消息处理函数：
![这里写图片描述](http://img.blog.csdn.net/20171104225220222?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
编辑OnLButtonDown及OnLButtonUp消息处理函数：

```
void Cday18Dlg::OnLButtonDown(UINT nFlags, CPoint point)
{
	// TODO: 在此添加消息处理程序代码和/或调用默认值
	if (point.x >= m_rtCtrl.left 
		&& point.x <= m_rtCtrl.right 
		|| point.y >= m_rtCtrl.top 
		&& point.y <= m_rtCtrl.bottom)
	{
		m_bCapturing = TRUE;
		SetCapture(); // 开始捕获鼠标
		SetCursor(m_hCursor);
	}
	CDialogEx::OnLButtonDown(nFlags, point);
}
```
代码解释：

> 1.判断鼠标点击的位置是否在图标上；
> 2.若是，则将开始捕获鼠标标志置位真，并且开始捕获鼠标位置；
> 3.将捕获的鼠标位置设置到成员变量m_hCursor；


```
void Cday18Dlg::OnLButtonUp(UINT nFlags, CPoint point)
{
	// TODO: 在此添加消息处理程序代码和/或调用默认值
	if (m_bCapturing)
	{
		ReleaseCapture();
		m_bCapturing = FALSE;
		POINT pt = point;
		ClientToScreen(&pt);
		m_hWndDest = ::WindowFromPoint(pt);
		TCHAR szBuf[MAX_PATH] = {0};
		_stprintf(szBuf,_T("0x%.8X"),m_hWndDest);
		SetDlgItemText(IDC_EDIT_DESTHWND,szBuf);
		GetClassName(m_hWndDest,szBuf,MAX_PATH);
		SetDlgItemText(IDC_EDIT_DESTCLASS,szBuf);
		::SendMessage(m_hWndDest,WM_GETTEXT,MAX_PATH,(LPARAM)szBuf);

		SetDlgItemText(IDC_EDIT_DESTTEXT,szBuf);
	}

	CDialogEx::OnLButtonUp(nFlags, point);
}
```

代码解释：

> 1.判断是否在捕获鼠标；
> 2.若是，释放鼠标捕获，获取当前鼠标的位置；
> 3.通过当前鼠标的位置获取到当前位置的窗口句柄；
> 4.分别获取该窗口的句柄，类名，标题；

效果图：
![这里写图片描述](http://img.blog.csdn.net/20171104230232355?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171104230242358?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 5.实现修改目标窗口标题
双击“修改标题”按钮，编辑其clicked方法：

```
void Cday18Dlg::OnBnClickedBtnSettext()
{
	// TODO: 在此添加控件通知处理程序代码
	CString strText;
	GetDlgItemText(IDC_EDIT_DESTTEXT,strText);
	::SendMessage(m_hWndDest,WM_SETTEXT,0,(LPARAM)(LPCTSTR)strText);
}
```
代码解释：

> 1.获取文本框中的标题值；
> 2.通过SendMessage方法发送WM_SETTEXT消息修改目标窗口的标题

效果图：
![这里写图片描述](http://img.blog.csdn.net/20171104230641050?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 6.实现关闭目标窗口
双击“关闭标题”按钮，编辑其clicked方法：

```
void Cday18Dlg::OnBnClickedBtnSettext2()
{
	// TODO: 在此添加控件通知处理程序代码
	::SendMessage(m_hWndDest,WM_CLOSE,0,0);
	//::PostMessage(m_hWndDest,WM_CLOSE,0,0);
}
```
代码解释：

> 1.通过SendMessage方法发送WM_CLOSE消息来关闭目标窗口；
> 


上面我们都是使用SendMessage方法来发送消息，其实我们也可以把SendMessage全部替换成PostMessage，我们来看看效果：
![这里写图片描述](http://img.blog.csdn.net/20171104231231467?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
我们可以看“窗口标题”获取的值是不对的，这是为什么？我们来看一下获取标题的这段代码：

```
		ReleaseCapture();
		m_bCapturing = FALSE;
		POINT pt = point;
		ClientToScreen(&pt);
		m_hWndDest = ::WindowFromPoint(pt);
		TCHAR szBuf[MAX_PATH] = {0};
		_stprintf(szBuf,_T("0x%.8X"),m_hWndDest);
		SetDlgItemText(IDC_EDIT_DESTHWND,szBuf);
		GetClassName(m_hWndDest,szBuf,MAX_PATH);
		SetDlgItemText(IDC_EDIT_DESTCLASS,szBuf);
		::PostMessage(m_hWndDest,WM_GETTEXT,MAX_PATH,(LPARAM)szBuf);
		SetDlgItemText(IDC_EDIT_DESTTEXT,szBuf);
```
我们看到前面获取窗口句柄，类名都是没问题的，但是到了最后获取标题时出了问题；
那是因为PostMessage是不会等待消息的返回结果，发送之后直接往下运行，这时szBuf的值还是前面获取的“窗口类名”，所以导致最后的“窗口标题”内容获取出错，这也很好的证明PostMessage和SendMessage的区别；
还有“修改标题”及“关闭窗口”按钮不管是PostMessage和SendMessage方法都不会出错，那是因为我们在这两个按钮方法中都不需要消息的返回值，所以在我们以后的实际使用中一定要考虑清楚需要使用哪种发送消息方法；

### 动态效果图：

![这里写图片描述](http://img.blog.csdn.net/20171104233147214?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
附MFC消息分类及说明：
### 窗口消息

> WM_CREATE           创建一个窗口 WM_DESTROY          当一个窗口被破坏时发送 WM_MOVE    
> 移动一个窗口 WM_SIZE             改变一个窗口的大小 WM_ACTIVATE        
> 一个窗口被激活或失去激活状态 WM_SETFOCUS         一个窗口获得焦点 WM_KILLFOCUS       
> 一个窗口失去焦点 WM_ENABLE           一个窗口改变成Enable状态 WM_SETREDRAW       
> 设置窗口是否能重画 WM_SETTEXT          应用程序发送此消息来设置一个窗口的文本 WM_GETTEXT         
> 应用程序发送此消息来复制对应窗口的文本到缓冲区 WM_GETTEXTLENGTH    得到与一个窗口有关的文本的长度（不包含空字符）
> WM_PAINT            要求一个窗口重画自己 WM_CLOSE           
> 当一个窗口或应用程序要关闭时发送一个信号 WM_QUERYENDSESSION 
> 当用户选择结束对话框或程序自己调用ExitWindows函数 WM_QUIT             用来结束程序运行
> WM_QUERYOPEN        当用户窗口恢复以前的大小位置时，把此消息发送给某个图标 WM_ERASEBKGND      
> 当窗口背景必须被擦除时（例在窗口改变大小时） WM_SYSCOLORCHANGE   当系统颜色改变时，发送此消息给所有顶级窗口
> WM_ENDSESSION       当系统进程发出WM_QUERYENDSESSION消息后，此消息发送给应用程序，通知它对话是否结束
> WM_SHOWWINDOW       当隐藏或显示窗口是发送此消息给这个窗口 WM_ACTIVATEAPP     
> 发此消息给应用程序哪个窗口是激活的，哪个是非激活的 WM_FONTCHANGE       当系统的字体资源库变化时发送此消息给所有顶级窗口
> WM_TIMECHANGE       当系统的时间变化时发送此消息给所有顶级窗口 WM_CANCELMODE      
> 发送此消息来取消某种正在进行的摸态（操作） WM_SETCURSOR       
> 如果鼠标引起光标在某个窗口中移动且鼠标输入没有被捕获时，就发消息给某个窗口 WM_MOUSEACTIVATE   
> 当光标在某个非激活的窗口中而用户正按着鼠标的某个键发送此消息给当前窗口 WM_CHILDACTIVATE   
> 发送此消息给MDI子窗口当用户点击此窗口的标题栏，或当窗口被激活，移动，改变大小 WM_QUEUESYNC       
> 此消息由基于计算机的训练程序发送，通过 WH_JOURNALPALYBACK 的 hook 程序分离出用户输入消息
> WM_GETMINMAXINFO    此消息发送给窗口当它将要改变大小或位置 WM_PAINTICON       
> 发送给最小化窗口当它图标将要被重画 WM_ICONERASEBKGND   此消息发送给某个最小化窗口，仅当它在画图标前它的背景必须被重画
> WM_NEXTDLGCTL       发送此消息给一个对话框程序去更改焦点位置 WM_SPOOLERSTATUS   
> 每当打印管理列队增加或减少一条作业时发出此消息 WM_DRAWITEM        
> 当button，combobox，listbox，menu的可视外观改变时发送 WM_MEASUREITEM      当button,
> combo box, list box, list view control, or menu item 被创建时
> WM_VKEYTOITEM      
> 此消息有一个LBS_WANTKEYBOARDINPUT风格的发出给它的所有者来响应WM_KEYDOWN消息 WM_CHARTOITEM   
> 此消息由一个LBS_WANTKEYBOARDINPUT风格的列表框发送给他的所有者来响应WM_CHAR消息 WM_SETFONT      
> 当绘制文本时程序发送此消息得到控件要用的颜色 WM_GETFONT          应用程序发送此消息得到当前控件绘制文本的字体
> WM_SETHOTKEY        应用程序发送此消息让一个窗口与一个热键相关连 WM_GETHOTKEY       
> 应用程序发送此消息来判断热键与某个窗口是否有关联 WM_QUERYDRAGICON   
> 此消息发送给最小化窗口，当此窗口将要被拖放而它的类中没有定义图标，应用程序能返回一个图标或光标的句柄，当用户拖放图标时系统显示这个图标或光标
> WM_COMPAREITEM      发送此消息来判定 combobox 或 listbox 新增加的项的相对位置
> WM_COMPACTING       显示内存已经很少了 WM_WINDOWPOSCHANGING  
> 发送此消息给那个窗口的大小和位置将要被改变时，来调用 setwindowpos 函数或其它窗口管理函数
> WM_WINDOWPOSCHANGED 发送此消息给那个窗口的大小和位置已经被改变时，来调用setwindowpos函数或其它窗口管理函数
> WM_POWER            当系统将要进入暂停状态时发送此消息 WM_COPYDATA        
> 当一个应用程序传递数据给另一个应用程序时发送此消息 WM_CANCELJOURNA     当某个用户取消程序日志激活状态，提交此消息给程序
> WM_NOTIFY           当某个控件的某个事件已经发生或这个控件需要得到一些信息时，发送此消息给它的父窗口
> WM_INPUTLANGCHANGEREQUEST  当用户选择某种输入语言，或输入语言的热键改变 WM_INPUTLANGCHANGE 
> 当平台现场已经被改变后发送此消息给受影响的最顶级窗口 WM_TCARD            当程序已经初始化 windows
> 帮助例程时发送此消息给应用程序 WM_HELP            
> 此消息显示用户按下了F1，如果某个菜单是激活的，就发送此消息个此窗口关联的菜单，否则就发送给有焦点的窗口，如果当前都没有焦点，就把此消息发送给当前激活的窗口
> WM_USERCHANGED     
> 当用户已经登入或退出后发送此消息给所有的窗口，当用户登入或退出时系统更新用户的具体设置信息，在用户更新设置时系统马上发送此消息
> WM_NOTIFYFORMAT     公用控件，自定义控件和他们的父窗口通过此消息来判断控件是使用ANSI还是UNICODE结构
> WM_CONTEXTMENU      当用户某个窗口中点击了一下右键就发送此消息给这个窗口 WM_STYLECHANGING   
> 当调用SETWINDOWLONG函数将要改变一个或多个 窗口的风格时发送此消息给那个窗口 WM_STYLECHANGED     当调用
> SETWINDOWLONG 函数一个或多个 窗口的风格后发送此消息给那个窗口 WM_DISPLAYCHANGE   
> 当显示器的分辨率改变后发送此消息给所有的窗口 WM_GETICON         
> 此消息发送给某个窗口来返回与某个窗口有关连的大图标或小图标的句柄 WM_SETICON         
> 程序发送此消息让一个新的大图标或小图标与某个窗口关联 WM_NCCREATE        
> 当某个窗口第一次被创建时，此消息在WM_CREATE消息发送前发送 WM_NCDESTROY       
> 此消息通知某个窗口，非客户区正在销毁 WM_NCCALCSIZE       当某个窗口的客户区域必须被核算时发送此消息
> WM_NCHITTEST        移动鼠标，按住或释放鼠标时发生 WM_NCPAINT         
> 程序发送此消息给某个窗口当它（窗口）的框架必须被绘制时 WM_NCACTIVATE      
> 此消息发送给某个窗口仅当它的非客户区需要被改变来显示是激活还是非激活状态 WM_GETDLGCODE      
> 发送此消息给某个与对话框程序关联的控件。正常情况下，windows 处理所有输入到此控件的箭头键和 TAB 键。通常响应
> WM_GETDLGCODE 消息，应用程序可以控制一个特定类型的输入和处理这个输入
>                      WM_NCMOUSEMOVE      当光标在一个窗口的非客户区内移动时发送此消息给这个窗口。非客户区为：窗体的标题栏及窗体的边框 WM_NCLBUTTONDOWN   
> 当光标在一个窗口的非客户区同时按下鼠标左键时提交此消息 WM_NCLBUTTONUP     
> 当用户释放鼠标左键同时光标某个窗口在非客户区十发送此消息 WM_NCLBUTTONDBLCLK 
> 当用户双击鼠标左键同时光标某个窗口在非客户区十发送此消息 WM_NCRBUTTONDOWN   
> 当用户按下鼠标右键同时光标又在窗口的非客户区时发送此消息 WM_NCRBUTTONUP     
> 当用户释放鼠标右键同时光标又在窗口的非客户区时发送此消息 WM_NCRBUTTONDBLCLK 
> 当用户双击鼠标右键同时光标某个窗口在非客户区十发送此消息 WM_NCMBUTTONDOWN   
> 当用户按下鼠标中键同时光标又在窗口的非客户区时发送此消息 WM_NCMBUTTONUP     
> 当用户释放鼠标中键同时光标又在窗口的非客户区时发送此消息 WM_NCMBUTTONDBLCLK 
> 当用户双击鼠标中键同时光标又在窗口的非客户区时发送此消息 WM_KEYFIRST         WM_KEYDOWN 按下一个键
> WM_KEYUP            释放一个键 WM_CHAR             按下某键，并已发出WM_KEYDOWN，
> WM_KEYUP消息 WM_DEADCHAR         当用 translatemessage 函数翻译 WM_KEYUP
> 消息时发送此消息给拥有焦点的窗口 WM_SYSKEYDOWN       当用户按住 ALT 键同时按下其它键时提交此消息给拥有焦点的窗口
> WM_SYSKEYUP         当用户释放一个键同时 ALT 键还按着时提交此消息给拥有焦点的窗口 WM_SYSCHAR      
> 当WM_SYSKEYDOWN消息被TRANSLATEMESSAGE函数翻译后提交此消息给拥有焦点的窗口 WM_SYSDEADCHAR    
> 当WM_SYSKEYDOWN消息被TRANSLATEMESSAGE函数翻译后发送此消息给拥有焦点的窗口 WM_INITDIALOG     
> 在一个对话框程序被显示前发送此消息给它，通常用此消息初始化控件和执行其它任务 WM_COMMAND         
> 当用户选择一条菜单命令项或当某个控件发送一条消息给它的父窗口，一个快捷键被翻译 WM_SYSCOMMAND      
> 当用户选择窗口菜单的一条命令或当用户选择最大化或最小化时那个窗口会收到此消息 WM_TIMER            发生了定时器事件
> WM_HSCROLL          当一个窗口标准水平滚动条产生一个滚动事件时发送此消息给那个窗口，也发送给拥有它的控件
> WM_VSCROLL          当一个窗口标准垂直滚动条产生一个滚动事件时发送此消息给那个窗口，也发送给拥有它的控件
> WM_INITMENU        
> 当一个菜单将要被激活时发送此消息，它发生在用户菜单条中的某项或按下某个菜单键，它允许程序在显示前更改菜单 WM_INITMENUPOPUP 
> 当一个下拉菜单或子菜单将要被激活时发送此消息，它允许程序在它显示前更改菜单，而不要改变全部 WM_MENUSELECT      
> 当用户选择一条菜单项时发送此消息给菜单的所有者（一般是窗口） WM_MENUCHAR        
> 当菜单已被激活用户按下了某个键（不同于加速键），发送此消息给菜单的所有者 WM_ENTERIDLE       
> 当一个模态对话框或菜单进入空载状态时发送此消息给它的所有者，一个模态对话框或菜单进入空载状态就是在处理完一条或几条先前的消息后没有消息它的列队中等待
> WM_CTLCOLORMSGBOX   在 windows
> 绘制消息框前发送此消息给消息框的所有者窗口，通过响应这条消息，所有者窗口可以通过使用给定的相关显示设备的句柄来设置消息框的文本和背景颜色
> WM_CTLCOLOREDIT     当一个编辑型控件将要被绘制时发送此消息给它的父窗口
> 通过响应这条消息，所有者窗口可以通过使用给定的相关显示设备的句柄来设置编辑框的文本和背景颜色 WM_CTLCOLORLISTBOX 
> 当一个列表框控件将要被绘制前发送此消息给它的父窗口
> 通过响应这条消息，所有者窗口可以通过使用给定的相关显示设备的句柄来设置列表框的文本和背景颜色 WM_CTLCOLORBTN     
> 当一个按钮控件将要被绘制时发送此消息给它的父窗口 通过响应这条消息，所有者窗口可以通过使用给定的相关显示设备的句柄来设置按纽的文本和背景颜色
> WM_CTLCOLORDLG      当一个对话框控件将要被绘制前发送此消息给它的父窗口
> 通过响应这条消息，所有者窗口可以通过使用给定的相关显示设备的句柄来设置对话框的文本背景颜色 WM_CTLCOLORSCROLLBAR 
> 当一个滚动条控件将要被绘制时发送此消息给它的父窗口 通过响应这条消息，所有者窗口可以通过使用给定的相关显示设备的句柄来设置滚动条的背景颜色
> WM_CTLCOLORSTATIC   当一个静态控件将要被绘制时发送此消息给它的父窗口 通过响应这条消息，所有者窗口可以
> 通过使用给定的相关显示设备的句柄来设置静态控件的文本和背景颜色 WM_MOUSEFIRST       移动鼠标时发生
> WM_MOUSEMOVE        移动鼠标时发生，同WM_MOUSEFIRST WM_LBUTTONDOWN      按下鼠标左键
> WM_LBUTTONUP        释放鼠标左键 WM_LBUTTONDBLCLK    双击鼠标左键 WM_RBUTTONDOWN  
> 按下鼠标右键 WM_RBUTTONUP        释放鼠标右键 WM_RBUTTONDBLCLK    双击鼠标右键
> WM_MBUTTONDOWN      按下鼠标中键 WM_MBUTTONUP        释放鼠标中键 WM_MBUTTONDBLCLK
> 双击鼠标中键 WM_MOUSEWHEEL       当鼠标轮子转动时发送此消息个当前有焦点的控件

### 按钮 

> BM_CLICK    按钮被点击消息  BM_GETCHECK 可用于复选框/单选框。查看是否被选择了  BM_GETSTATE
> 发送此消息，可返回 button 的状态，如是否被选择；是否可用（不可用就变灰了）  BM_SETCHECK
> 如果已经选择了，发送此消息后，变为未选择，就是那个钩没被勾上 BM_SETSTATE 设置 button 被点击状态。

### 组合框 
 

> CB_ADDSTRING       添加字符串到组合框。  CB_DELETESTRING    删除组合框中的条目，即 item 。
> CB_GETCOUNT        得到组合框条目 item 的数目。  CB_GETCURSEL      
> 返回组合框中被选条目在组合框中的位置，第一条为 0。
>                    如果没有条目或出错，则返回 -1 。 CB_GETDROPPEDSTATE 发送此消息，可判断组合框的下拉列表是否下拉。
>                    如果是，返回非零值，不是，则返回 0 。 CB_GETLBTEXT       得到组合框的条目文本。返回值是这个文本的长度。  CB_GETLBTEXTLEN    返回值是条目的文本的长度。 
> CB_INSERTSTRING    插入字符串条目到组合框中。  CB_RESETCONTENT    清空组合框所有条目。 
> CB_SETCURSEL       设置组合框被选条目。  CB_SHOWDROPDOWN    让组合框的下拉列表下拉，即显出所有条目。

### 编辑框 
 

> EM_CANUNDO             决定上一次操作是否可以 undo（撤消操作）。如果可以，则可发送 EM_UNDO 消息   
> EM_GETFIRSTVISIBLELINE 在多行控件中，找到最上层的可见的行号。此行号是相对于所有行的。 
> EM_GETPASSWORDCHAR     返回密码框的字符集，即查看密码。  EM_GETSEL             
> 返回在可编辑控件中，被选择（高亮选择）的字符集的起点和终点的位置，用 SendMessage 的 wParam
> 参数返回起点位置，lParam 返回终点位置  EM_REPLACESEL         
> 用不同的字符串替换可编辑控件中的字符串。如果可编辑控件中没有字符串，则此消息变为添加字符串。如果 wParam 为
> TRUE，则本次操作允许撤消，FALSE 禁止撤消。  EM_SETPASSWORDCHAR     在可编辑控件中设置密码字符集，即用 *
> 代替  EM_UNDO                发送操作撤消消息。    EM_GETLINE            
> 获取编辑控件中输入的文字。 EM_LINEFROMCHAR        检索指定字符索引（索引编号从编辑框的第一个字符开始）所在的行索引
> EM_LINEINDEX           在多行编辑控件中，检索某行首字符在编辑控件中的索引 EM_ERRSPACE          
> 编辑控件不能分配足够的内存来满足特定的要求。
>                        编辑控件的父窗口通过 WM_COMMAND 消息收到此消息。 EM_LIMITTEXT           设置编辑框用户可输入的最大字符数。wParam 为字符数，lParam 不使用(0L)

### IP 地址控件 
 

> IPM_CLEARADDRESS       清除 IP 地址控件（IP Address control）的内容 
> IPM_GETADDRESS         从 IP 地址控件获得存储在它中的 IP 地址信息 IPM_ISBLANK          
> 决定 IP 地址控件是否可以为空值。即 127.0.0.1 之类的地址为空  IPM_SETADDRESS         在 IP
> 地址控件中设置 IP 地址     IPM_SETFOCUS           在 IP 地址控件中，当需要输入 IP 地址时，
> 使之获得键盘输入焦点  IPM_SETRANGE           设置输入 IP 地址的有效范围

### MCI（Media Control Interface) 

> MM_MCINOTIFY           该 MM_MCINOTIFY 消息通知应用程序，一个 MCI 设备已完成操作。只有设置了
> MCI_NOTIFY 标志时，MCI 设备才发送此消息。

### 菜单

> WM_COMMAND     当用户选择菜单中的项目后,将向窗体发送此消息. 窗体收到此消息后,再决定下一个行为。 WM_INITMENU 
> 当菜单准备显示前,向窗体发送此消息, 窗体将初始化菜单项。  WM_SYSCOMMAND  向窗体发送用户点击系统菜单消息.
> 窗体将响应这个消息 ,决定下个行为。

### 列表框

> LB_ADDSTRING        在条目中添加字符串  LB_DELETESTRING     删除一个条目. 条目序号是从 0
> 开始的.  LB_GETCOUNT         得到条目总数.  LB_GETCURSEL        得到单选的列表框选项条目的序号
> LB_GETSEL           判断列表框的条目是否被选上, 如果选上了,则返回 >0 的值。否则返回 0 ,表示用户没选择条目 
> LB_GETSELCOUNT      获得可多选的列表框中被选择的条目数  LB_GETSELITEMS     
> 返回可多选的列表框中被选条目的序号，可返回数组 LB_GETTEXT          得到列表框中的一个条目的文本 
> LB_GETTEXTLEN       得到列表框中的一个条目的文本的长度  LB_INSERTSTRING    
> 在列表框中插入一个条目。如果成功，将返回插入后此条目的序号。  LB_SETCURSEL       
> 对单选的列表框，设定用户选择条目的具体值  LB_SETSEL           对多选的列表框，设定用户选择条目的具体值 
> LB_RESETCONTENT     从列表框删除所有项目，wParam 和 lParam 参数均不使用（为 0）
> LB_SETHORIZONTALEXTENT
> 设定列表框水平滚动范围。如果列表框宽度小于此值，则水平滚动条显现；如果列表框宽度大于等于此值，则水平滚动条是隐藏的。wParam
> 为所设的水平滚动范围（像素），lParam 不使用，为 0。没有返回值 注意：LB_SETHORIZONTALEXTENT
> 消息要起作用，列表框必须定义 WS_HSCROLL 样式 LB_SETTABSTOPS     
> 在列表框中设置制表位位置（即每列间距）为了应对 LB_SETTABSTOPS 消息，列表框必须已经拥有 LBS_USETABSTOPS
> 样式。 wParam 指定制表位数量，lParam 为制表位整数数组（各列之间间隔，不必相等）如果 wParam 是 0，lParam 为
> NULL，默认制表位是 2 个对话框模板单位。如果 wParam 是 1，制表位为 lParam 指定的距离。如果超过 1，制表位将被设置为
> lParam 中的每个值（wParam 指定数量）

### 鼠标 

> WM_LBUTTONDBLCLK  当鼠标在一个窗体范围内时，告诉此窗体鼠标左键已双击，返回值 0  WM_LBUTTONDOWN   
> 当鼠标在一个窗体范围内时，告诉此窗体鼠标左键已点击，返回值 0  WM_LBUTTONUP     
> 当鼠标在一个窗体范围内时，告诉此窗体鼠标左键已释放，返回值 0   WM_MBUTTONDBLCLK 
> 当鼠标在一个窗体范围内时，告诉此窗体鼠标中键已双击，返回值 0  WM_MBUTTONDOWN   
> 当鼠标在一个窗体范围内时，告诉此窗体鼠标中键已点击，返回值 0  WM_MBUTTONUP     
> 当鼠标在一个窗体范围内时，告诉此窗体鼠标中键已释放，返回值 0


### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)

### [>>>我的私人博客<<<](http://amuuncle.site/)


