---
title: 第13节 MFC之图片控件
date: 2017-10-31 22:37:27
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# 第13节 MFC之图片控件

这节学习两个控件：

> 图片控件：  Picture Control

## 1. 新建项目
新建一个基于对话框项目“day15”，布局如下，自行处理：
![这里写图片描述](http://img.blog.csdn.net/20171031214935166?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
拖动一个**Picture Control**控件到界面，其实Picture Control就是CStatic 类；

设置**Picture Control**的如下属性：

| 属性|             修改值|             解释 | 
| --------   |--------         |  -----:  |
| ID     | IDC_STATIC_IMG     |         控件ID| 
| Type   |   Bitmap |  设置类型为bitmap位图类型| 
如图：![这里写图片描述](http://img.blog.csdn.net/20171031215325005?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 2.添加Bitmap 位图资源
自行下载几张.bmp位图，拷贝到项目的res文件下，然后切换到资源视图，添加Bitmap 资源，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171031220313389?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171031220321254?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171031220331105?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
上传完成之后可以看到已经有三个Bitmap 位图的ID；
![这里写图片描述](http://img.blog.csdn.net/20171031220405693?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 3.显示出位图资源
单击**Picture Control**控件，在属性中找到Image属性，在下拉框中选择我们刚才添加的位图ID就可以成功显示图片了，如图：
![这里写图片描述](http://img.blog.csdn.net/20171031220811037?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 4.动态控制显示图片
在界面上添加一个按钮，我么通过按钮来切换界面图片显示：
![这里写图片描述](http://img.blog.csdn.net/20171031221205220?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
接下来我们添加**Picture Control**控件的变量m_image，如图:
![这里写图片描述](http://img.blog.csdn.net/20171031221246177?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
我们来编辑“切换按钮”的点击方法：

```
void Cday15Dlg::OnBnClickedButtonChange()
{
	// TODO: 在此添加控件通知处理程序代码
	HBITMAP phBmp = (HBITMAP)LoadImage(NULL,_T(".\\res\\20171031100114614.bmp"),IMAGE_BITMAP,0,0,LR_LOADFROMFILE);
	m_image.SetBitmap(phBmp);
}
```
代码解释：

> 1. 获取一个位图的句柄
> 2.将其设置到**Picture Control**控件

效果图：
![这里写图片描述](http://img.blog.csdn.net/20171031222147848?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 5.配合CFileDialog 类来选择显示图片
我们来编辑“切换按钮”的点击方法：

```
void Cday15Dlg::OnBnClickedButtonChange()
{
	// TODO: 在此添加控件通知处理程序代码
	CFileDialog dlg(TRUE,NULL,NULL,OFN_FILEMUSTEXIST,_T("*.bmp|*.bmp"),this);
	if (dlg.DoModal() == IDOK)
	{
		HBITMAP phBmp = (HBITMAP)LoadImage(NULL,dlg.GetPathName(),IMAGE_BITMAP,0,0,LR_LOADFROMFILE);
		m_image.SetBitmap(phBmp);
	}
}
```
代码解释：

> 1. 创建一个.bmp类型的文件打开对话框
> 2.  若点击确定按钮，则将选择的.bmp文件显示出来；

效果图：
![这里写图片描述](http://img.blog.csdn.net/20171031223111658?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

附**Picture Control**控件常见属性及方法：
### 一、图片控件属性

> Picture Control 属性: Type:Frame //框架 Type:Etched Horz水平蚀刻线条 Type:Etched
> Vert垂真蚀刻线条 Type:Rectangle实心矩形 Type:Bitmap位图 Type:Icon  图标
> Type:Enhanced Metafile 增强图元 支持wmf格式图片 Type:Owner Draw   自绘图 Color:颜色
>     Black:黑
>     Gray:灰色
>     White:白色
>     Etched:蚀刻

### 二、Picture Control 控件类

> CStatic:: SetBitmap Specifies a bitmap to be displayed in the static
> control. GetBitmap Retrieves the handle of the bitmap previously set
> with SetBitmap.
> 
> SetIcon Specifies an icon to be displayed in the static control.
> GetIcon Retrieves the handle of the icon previously set with SetIcon.
> 
> SetCursor Specifies a cursor image to be displayed in the static
> control. GetCursor Retrieves the handle of the cursor image previously
> set with SetCursor.
> 
> SetEnhMetaFile Specifies an enhanced metafile to be displayed in the
> static control. GetEnhMetaFile Retrieves the handle of the enhanced
> metafile previously set with SetEnhMetaFile



### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)

### [>>>我的私人博客<<<](http://blog.amuuncle.site/)
