---
title: 第4节 MFC消息映射机制
date: 2017-10-28 23:30:28
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# Windows编程基础--第4节 MFC消息映射机制
对于MFC程序最重要的响应机制就是消息映射机制，这节我们就来一起尝试一下MFC的消息映射机制。
（操作系统：win10 64位 IDE：vc++ 6.0） 
1、新建一个MFC对话框项目，参见上节，
2、编译代码运行，效果图如下：
![这里写图片描述](http://img.blog.csdn.net/20171020220853804?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
3、现在我们删除对话框上的《确定》和《取消》按钮，如图：
![这里写图片描述](http://img.blog.csdn.net/20171020221041426?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
4、现在我们添加自己的“OK”和“CANCEL”按钮，接下来我们就来看看“OK”按钮的按下消息是怎么进行处理的？
![这里写图片描述](http://img.blog.csdn.net/20171020221432827?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
4、执行View->Class Wizard,打开类向导；（或者直接用ctrl + W）

此时就能看到我们创建的对话框，OK按钮，CANCEL按钮对象，点击它们可以看见它们分别的拥有的消息，如图：

![这里写图片描述](http://img.blog.csdn.net/20171020222144280?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
5、我们选择Cday03Dlg，MESSAGES选择WM_MOUSEMOVE消息，点击Add Function，下部Member function就会出现与WM_MOUSEMOVE对应的OnMouseMove函数，接下来点击Edit Code，编辑OnMouseMove函数的内容：
![这里写图片描述](http://img.blog.csdn.net/20171020223001512?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171020223015497?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
6、我们来修改OnMouseMove(UINT nFlags, CPoint point) 函数，参数中point为鼠标的坐标位置，我们可以通过point.x, point.y来获取鼠标的位置，nFlags主要是标志一些控制键是否按下，然后MK_LBUTTON、MK_RBUTTON、MK_CONTROL、MK_SHIFT、MK_MBUTTON 分别对应鼠标左键，右键，CTRL ，SHIFT ，鼠标中间（转轮）：
```
void CDay03Dlg::OnMouseMove(UINT nFlags, CPoint point) 
{
	// TODO: Add your message handler code here and/or call default
	CString strText;
	strText.Format("坐标 x = %d ,y = %d ",point.x, point.y);

	if (nFlags & MK_LBUTTON)
	{
		strText += " 鼠标左键DOWN";
	}
	if (nFlags & MK_RBUTTON)
	{
		strText += " 鼠标右键DOWN";
	}
	if (nFlags & MK_CONTROL)
	{
		strText += " CTRL DOWN";
	}
	if (nFlags & MK_SHIFT)
	{
		strText += " SHIFT DOWN";
	}
	if (nFlags & MK_MBUTTON)
	{
		strText += " MIDBUTTON DOWN";
	}
	SetWindowText(strText);  // 设置对话框标题文本

	CDialog::OnMouseMove(nFlags, point);
}
```
效果图：
![这里写图片描述](http://img.blog.csdn.net/20171020224733563?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

7、同样，我们可以通过类向导分别设置“OK”，“CANCEL”按钮的消息触发函数；
![这里写图片描述](http://img.blog.csdn.net/20171020225549041?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171020225556702?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171020225608346?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

8、这是我们其实可以看到在day03Dlg.cpp中MESSAGE_MAP总下方就有我们新增的三个MFC消息，并且可以直观的看出是属于哪个控件ID的；

```
BEGIN_MESSAGE_MAP(CDay03Dlg, CDialog)
	//{{AFX_MSG_MAP(CDay03Dlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_WM_MOUSEMOVE()
	ON_BN_CLICKED(IDC_BUTTON_OK, OnButtonOk)
	ON_BN_CLICKED(IDC_BUTTON_CACEL, OnButtonCacel)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()
```
9、接下来我们切换到day03Dlg.h头文件中，所有afx_msg 开头的都是消息对应的处理函数：

```
	// Generated message map functions
	//{{AFX_MSG(CDay03Dlg)
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnMouseMove(UINT nFlags, CPoint point);
	afx_msg void OnButtonOk();
	afx_msg void OnDoubleclickedButtonCacel();
	afx_msg void OnButtonCacel();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
```
10、由以上例子可以看出，MFC程序的消息映射机制是创建一个与窗口相关联的派生类，用于消息关联的成员函数来接收和处理窗口的消息。在类向导中选择对应的消息，添加与该消息关联的成员函数来处理该消息，这就是MFC的消息映射机制。具体控件或窗口支持哪些消息及消息对应的函数参数等，请参见MSDN；
11、最终效果图：
![这里写图片描述](http://img.blog.csdn.net/20171020232524462?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

[项目源码可以访问我的码云来fork](https://gitee.com/AmuUncle/MFC_CSDN.git "项目源码可以访问我的码云来fork")






