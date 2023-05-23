---
title: 第14节 MFC之文件对话框CFileDialog
date: 2017-11-01 21:49:20
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# 第14节 MFC之文件对话框CFileDialog


----------


今天我们学习两个打开文件对话框、保存文件对话框，应用程序难免需要加载文件，或者打开配置文件等，这就用到打开或者保存对话框，例如windows文本编辑器中保存对话框就属于其中一种：
![这里写图片描述](http://img.blog.csdn.net/20171101203217131?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


----------
## 1. 新建项目
新建一个基于对话框项目“day16”，布局如下，自行处理： 
![这里写图片描述](http://img.blog.csdn.net/20171101203650950?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
拖动一个EDIT到界面，并修改如下属性：

| 属性|             修改值|             解释 | 
| --------   |--------         |  -----  |
| ID| IDC_EDIT_TXT| 控件ID| 
| Want Return |   TRUE   | 允许回车| 
|Multiline      |   TRUE   |  允许多行| 
|Horizontal Scoll|   TRUE   |  水平滚动条| 
|Vertical Scoll|   TRUE   |  垂直滚动条| 

## 2. 添加菜单资源
切换到资源视图，添加菜单资源如下：
![这里写图片描述](http://img.blog.csdn.net/20171101204453007?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
若不知道怎么添加菜单请参考[**Windows编程基础--第10节 MFC菜单 **](http://blog.csdn.net/qq_25549309/article/details/78359647)

> 注意：菜单选项最后加上&符号可以设置快捷键，如“文件(&F)”，当程序运行时可以通过ALT + F快捷打开文件菜单选项；

将菜单绑定到主界面：
![这里写图片描述](http://img.blog.csdn.net/20171101204853878?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3. 实现文件打开对话框
右击菜单中“打开”选项，选择“添加事件处理处理程序”，添加处理程序，如图：
![这里写图片描述](http://img.blog.csdn.net/20171101205350070?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)其中行数处理程序名称：OnFileOpen，类列表选择：Cday16Dlg，添加编辑：
函数代码如下：

```
void Cday16Dlg::OnFileOpen()
{
	// TODO: 在此添加命令处理程序代码
	CFileDialog dlg(TRUE,NULL,NULL,OFN_FILEMUSTEXIST|OFN_PATHMUSTEXIST,_T("文本文件(*.txt)|*.txt|所有文件(*.*)|*.*||"),this);
	dlg.m_ofn.lpstrInitialDir = _T("C:\\");
	if (dlg.DoModal()  == IDOK)
	{
		CStdioFile inFile;
		inFile.Open(dlg.GetPathName(),CFile::modeRead);
		CString text;
		CString temp;
		while(inFile.ReadString(text))
		{    
			GetDlgItemText(IDC_EDIT_TXT,temp);
			if (temp.GetLength() > 0)
			{
				SetDlgItemText(IDC_EDIT_TXT,temp +"\r\n"+ text);
			}
			else
			{
				SetDlgItemText(IDC_EDIT_TXT,text);
			}
			
		}

		inFile.Close();
	}
}
```
代码解释：

> 1. 创建一个txt文件对话框；
> 2. 如文件对话框确定按钮被点击，则打开文件位置，文件全路径就是dlg.GetPathName()；
> 3. 循环读取文件，知道文件读取结束；每读一行就先获取界面文本框的内容加上新读取的文本，重新设置到界面；
> 4. 关闭文件

这样一个打开文件对话框就完成了，效果图如下：
![这里写图片描述](http://img.blog.csdn.net/20171101213305582?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3. 实现文件保存对话框
右击菜单中“保存”选项，选择“添加事件处理处理程序”，添加处理程序，如图：
![这里写图片描述](http://img.blog.csdn.net/20171101213433187?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
名称：OnSaveFile，类列表选择：Cday16Dlg，添加编辑：
函数代码如下
```
void Cday16Dlg::OnSaveFile()
{
	// TODO: 在此添加命令处理程序代码
	CFileDialog dlg(FALSE,NULL,NULL,OFN_HIDEREADONLY |OFN_OVERWRITEPROMPT | OFN_PATHMUSTEXIST,_T("文本文件(*.txt)|*.txt||"),this);
	if (dlg.DoModal()  == IDOK)
	{
		CFile file;  //建立一个CFile对象
		//打开文件,如果不存在该文件就创建文件
		if(!file.Open(dlg.GetPathName(),CFile::modeCreate|CFile::modeWrite))
		{
			AfxMessageBox( "can   not   Create   file! ");
			return;
		} 

		CString output;
		GetDlgItemText(IDC_EDIT_TXT,output);
		file.Write(output,strlen(output));
		file.Flush();    //将在缓冲区中的字符写入文件中
		file.Close();   //关闭文件
		AfxMessageBox( "保存成功！");
	}
}
```
代码解释：

> 1. 创建一个txt文件保存对话框；
> 2. 如文件对话框确定按钮被点击，则获取文件位置，文件全路径就是dlg.GetPathName()；
> 3. 先获取界面文本框的内容，将内容写到文件中；
> 4. 关闭文件
效果图：
![这里写图片描述](http://img.blog.csdn.net/20171101214549676?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


好了，这节我们演示了如何创建文件打开和保存对话框，希望对大家有作用，今天就到这了。
----------
### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)

### [>>>我的私人博客<<<](http://blog.amuuncle.site/)