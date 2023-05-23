---
title: Windows编程基础--第1节  第一个win32软件
date: 2017-10-28 22:42:12
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# Windows编程基础--第1节  第一个win32软件

下面新建一个win32程序，来演示win32程序开发的原理
（操作系统：win10 64位    IDE：vc++ 6.0）
 1、执行File -> new命令，来新建一个工程，如下图：
 ![这里写图片描述](http://img.blog.csdn.net/20171017222046015?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 2、点击 OK按钮，然后选择A simple win32 application，单击Finish完成创建；
 ![这里写图片描述](http://img.blog.csdn.net/20171017222259506?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
3、此时右边项目视图会显示我们刚才创建好的项目，双击Globals下面的WinMain函数
 ![这里写图片描述](http://img.blog.csdn.net/20171017222422511?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 4、现在来新建一个简单的对话框
	

```
 MessageBox(NULL,"Hello World!!","My First Win32 App",MB_OK);
```
![这里写图片描述](http://img.blog.csdn.net/20171017223030168?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
5、单击状态栏上的 “build”，或者直接按<F7>键进行编译，然后单击状态栏的 ！ 来运行程序，或者ctrl+F5;
![这里写图片描述](http://img.blog.csdn.net/20171017223404504?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
以下是MessageBox的原型：

```
int WINAPI MessageBox(
  HWND hWnd,          // handle of owner window
  LPCTSTR lpText,     // address of text in message box
  LPCTSTR lpCaption, // address of title of message box
  UINT uType          // style of message box
);
```
hWnd是消息框的拥有窗口。如果此参数为NULL，则消息框没有拥有窗口。
lpText为消息框的内容。
lpCaption为消息框的标题。
uType指定一个决定对话框的内容和行为（按钮、图标、形态及其他）的位标志集。
附其它常用属性 

系统默认图标，可在消息框上显示 
X错误 MB_ICONHAND, MB_ICONSTOP, and MB_ICONERROR 
?询问 MB_ICONQUESTION 
!警告 MB_ICONEXCLAMATION and MB_ICONWARNING 
i信息 MB_ICONASTERISK and MB_ICONINFORMATION 

按钮的形式 

MB_OK 默认 
MB_OKCANCEL 确定取消 
MB_YESNO 是否 
MB_YESNOCANCEL 是否取消 

返回值 

IDCANCEL 取消被选 
IDNO 否被选 
IDOK 确定被选 
IDYES 是被选 
6、对照函数说明，我们可以简单根据对话框返回值来执行不同的代码，如图：

```
#include "stdafx.h"

int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
 	// TODO: Place code here.
	int ret = MessageBox(NULL,"Hello World!!","My First Win32 App",MB_OKCANCEL );
	if(IDCANCEL == ret)
	{
		MessageBox(NULL,"CANCEL is clicked","My First Win32 App",MB_OK);
	}
	else if(IDOK  == ret)
	{
		MessageBox(NULL,"OK is clicked","My First Win32 App",MB_OK);
	}
	return 0;
}
```

![这里写图片描述](http://img.blog.csdn.net/20171017225111741?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


项目源码可以访问我的码云来fork：

```
https://gitee.com/AmuUncle/MFC_CSDN.git
```