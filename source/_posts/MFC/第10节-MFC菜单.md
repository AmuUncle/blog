---
title: 第10节 MFC菜单
date: 2017-10-28 23:33:24
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# Windows编程基础--第10节 MFC菜单


# MFC菜单（CMenu）

MFC菜单分为两类：

> 窗体菜单 
> 快捷菜单:又叫弹出菜单，或者上下文菜单

### 1、创建项目
打开vs2010，创建一个基于对话框的项目，项目名“day10”,注意这次主框架中就不要勾选“系统菜单”和“关于框”了，如图：
![这里写图片描述](http://img.blog.csdn.net/20171026223157074?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
创建好后，删除自动生成的文本控件，如图：
![这里写图片描述](http://img.blog.csdn.net/20171026223358413?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 2、创建系统菜单
切换到资源视图，右击我们的项目“day10”，选择添加资源，出现如下界面：
![这里写图片描述](http://img.blog.csdn.net/20171026223840662?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![这里写图片描述](http://img.blog.csdn.net/20171026223849482?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
选择“Menu”点击新建,然后就可以看到我们的项目中Menu目录，这里就存放菜单资源，展开后就可以看到，我们刚添加的菜单ID，双击打开；
我们可以直接输入想要添加的菜单选项，如图：
![这里写图片描述](http://img.blog.csdn.net/20171026225016056?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
我们可以在资源视图右击菜单ID，然后选择属性，修改ID为IDR_MENU_SYSTEM;
### 3、显示系统菜单
我们打开刚才创建的主窗口，右击打开属性，在属性列表找到MENU属性，下拉框选择刚才创建的IDR_MENU_SYSTEM菜单，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171026225352426?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
这时主窗口就和IDR_MENU_SYSTEM菜单关联起来了，运行看看效果：
![这里写图片描述](http://img.blog.csdn.net/20171026225644814?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 4、创建菜单消息事件
我们切换到我们创建的菜单界面，来实现菜单中保存选项的处理事件，在“保存”选项上右击，选择“添加事件处理函数”，如下：
![这里写图片描述](http://img.blog.csdn.net/20171026225912317?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
，出现如下添加事件界面：
![这里写图片描述](http://img.blog.csdn.net/20171026230051574?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
这里我们类列表中选择Cday10Dlg中创建操作函数，函数名修改为OnMenuSaveClick，点击“添加编辑”，添加处理函数；

```
void Cday10Dlg::OnMenuSaveClick()
{
	// TODO: 在此添加命令处理程序代码
	AfxMessageBox(_T("文件已保存！"));  
}
```
运行效果，点击“文件”->“保存”,此时就会弹窗提示“”"文件已保存！"，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171026230628546?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 5、创建快捷菜单
切换资源视图，
选择“Menu”点击“插入MENU”,自动打开；我们可以直接输入想要添加的菜单选项，如图：
![这里写图片描述](http://img.blog.csdn.net/20171026231003422?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
注意：快捷菜单中最上面的“快捷菜单”不会显示，名字可以随意。
修改次menu的ID为IDR_MENU_QUICK；

### 6、显示快捷菜单
我们打开刚才创建的主窗口，右击打开属性，在属性列表上方选择“消息”![这里写图片描述](http://img.blog.csdn.net/20171026234537989?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)按钮，找到“WM_OnContextMenu”,选择add OnContextMenu方法，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171026231615024?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

```
void Cday10Dlg::OnContextMenu(CWnd* pWnd, CPoint point)
{
	// TODO: 在此处添加消息处理程序代码
	CMenu menu;
	if(!menu.LoadMenu(IDR_MENU_QUICK))
	{
		return;
	}
	CMenu* pMenu = menu.GetSubMenu(0);
	pMenu->TrackPopupMenu(TPM_LEFTALIGN|TPM_RIGHTBUTTON,point.x,point.y,pWnd);
}
```
这段代码的意思就是：先试图加载IDR_MENU_QUICK菜单，加载成功之后，将菜单显示在鼠标右击（TPM_RIGHTBUTTON），靠左方（TPM_LEFTALIGN）的位置；
运行效果：
![这里写图片描述](http://img.blog.csdn.net/20171026232302952?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
可以看见，菜单已经显示出来；

### 7、创建菜单消息事件
同步骤4，如图：
![这里写图片描述](http://img.blog.csdn.net/20171026232540747?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
编辑OnCopy函数，如下：

```
void Cday10Dlg::OnCopy()
{
	// TODO: 在此添加命令处理程序代码
		AfxMessageBox(_T("文件已复制！"));  
}
```
效果图：
![这里写图片描述](http://img.blog.csdn.net/20171026232658919?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)



