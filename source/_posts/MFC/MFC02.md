---
title: Windows编程基础--第2节 win32程序资源管理
date: 2017-10-28 22:55:13
type: "categories"
categories: MFC从入门到放弃
tags: MFC
---
# Windows编程基础--第2节 win32程序资源管理
（操作系统：win10 64位 IDE：vc++ 6.0） 
windows程序都有自己的资源，例如按钮，图标，对话框等等，这节介绍如何使用win32程序资源管理；
1、继续使用上节的win32程序demo，执行File->new添加资源，选择Files选项卡中的Resource Script，填写资源名，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171018195816455?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
2、此时项目左侧会出现ResourceView视图，单击ResourceView中的根节点+号，会提示“This file is already open in an editor”，这时候关闭右边的day01.rc，再次打开就可以了；
![这里写图片描述](http://img.blog.csdn.net/20171018200304399?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
3、在ResourceView节点day01 Resources节点上右击->Insert,选中Dialog
,单击“New”,创建一个对话框资源，创建成功之后如图：
![这里写图片描述](http://img.blog.csdn.net/20171018200805292?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
4、在新建的对话框上右击选择属性（Properties），会弹出dialog的属性窗口，可以设置一些对话框的相关属性，如图
![这里写图片描述](http://img.blog.csdn.net/20171018201154122?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
5、接下来我们做一个简单的BMI计算器(体重指数BMI=体重/身高的平方（国际单位kg/㎡）)，拖动三个Edit分别用来显示身高，体重，BMI值，并设置属性ID，分别为：IDC_EDIT_SG、IDC_EDIT_TZ,IDC_EDIT_BMI，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171018204956574?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
6、接下来切换到类视图（classView），双击WinMain入口函数，添加对话框语句：

```
DialogBox(hInstance,(LPCTSTR)IDD_DIALOG_BMI,NULL,DlGFUNC);
```
其中IDD_DIALOG_BMI为刚才添加的对话框属性ID，DlGFUNC为对话框的消息处理函数，
7、接下来我们添加DlGFUNC函数，如下：

```
BOOL CALLBACK DlGFUNC(HWND hwnd_dlg,UINT uMsg,WPARAM wParam,LPARAM lParam)
{
	switch(uMsg)
	{
	case WM_COMMAND:
		switch(wParam)
		{
		case IDCANCEL:
			EndDialog(hwnd_dlg,IDCANCEL);
			break;
		case IDOK:
			{
				int nHeight= GetDlgItemInt(hwnd_dlg,IDC_EDIT_SG,NULL,TRUE);
				double dHeight = nHeight / 100.00;
				int nWeight = GetDlgItemInt(hwnd_dlg,IDC_EDIT_TZ,NULL,TRUE);
				double bmi = nWeight/(dHeight*dHeight);
				char buf[28];
				sprintf(buf, "%.3f", bmi);
				SetDlgItemText(hwnd_dlg,IDC_EDIT_BMI,buf);
			}
			break;
		}
		break;
	}
	return FALSE;
}
```
其中IDOK，和IDCANCEL为对话框确认按钮和取消按钮所触发消息，IDCANCEL关闭对话框，IDOK消息我们来获取身高和体重Edit中的值，并按照公式体重指数BMI=体重/身高的平方（国际单位kg/㎡）计算BMI,最后将BMI值设置到BMI  Edit中：

```
				int nHeight= GetDlgItemInt(hwnd_dlg,IDC_EDIT_SG,NULL,TRUE);
				double dHeight = nHeight / 100.00;
				int nWeight = GetDlgItemInt(hwnd_dlg,IDC_EDIT_TZ,NULL,TRUE);
				double bmi = nWeight/(dHeight*dHeight);
				char buf[28];
				sprintf(buf, "%.3f", bmi);
				SetDlgItemText(hwnd_dlg,IDC_EDIT_BMI,buf);
```
注意：要在文件头部引用资源头文件：#include "resource.h"
最终效果如下：
![这里写图片描述](http://img.blog.csdn.net/20171018210021527?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
附day01.cpp源码：

```
// day01.cpp : Defines the entry point for the application.
//

#include "stdafx.h"
#include "resource.h"
#include "stdio.h"


BOOL CALLBACK DlGFUNC(HWND hwnd_dlg,UINT uMsg,WPARAM wParam,LPARAM lParam)
{
	switch(uMsg)
	{
	case WM_COMMAND:
		switch(wParam)
		{
		case IDCANCEL:
			EndDialog(hwnd_dlg,IDCANCEL);
			break;
		case IDOK:
			{
				int nHeight= GetDlgItemInt(hwnd_dlg,IDC_EDIT_SG,NULL,TRUE);
				double dHeight = nHeight / 100.00;
				int nWeight = GetDlgItemInt(hwnd_dlg,IDC_EDIT_TZ,NULL,TRUE);
				double bmi = nWeight/(dHeight*dHeight);
				char buf[28];
				sprintf(buf, "%.3f", bmi);
				SetDlgItemText(hwnd_dlg,IDC_EDIT_BMI,buf);
			}
			break;
		}
		break;
	}
	return FALSE;
}

int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
 	// TODO: Place code here.
	DialogBox(hInstance,(LPCTSTR)IDD_DIALOG_BMI,NULL,DlGFUNC);

	return 0;
}
```
后记：
	DialogProc是一个窗口过程函数。该函数为一个应用程序定义可与DialogBox函数一起使用的回调函数。它处理发送到一个模态的或无模式对话框的消息。DLGPROC类型定义了一个指向此回调函数的指针。DialogProc函数是应用程序定义函数名的一个占位符。
函数原型：

```
BOOL CALLBACK DialogProc(
HWND hwndDlg,
UINT UMsg,
WPARAM wParam,
LPARAM lParam
);
```

hwndDlg
指定对话框。
uMsg
指定消息。
wParam
指定消息特定的其他信息。
Iparam
指定消息特定的其他信息。

项目源码可以访问我的码云来fork：

```
https://gitee.com/AmuUncle/MFC_CSDN.git
```