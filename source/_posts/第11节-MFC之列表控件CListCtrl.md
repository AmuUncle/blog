---
title: 第11节 MFC之列表控件CListCtrl
date: 2017-10-29 21:14:48
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---

# Windows编程基础--第11节 MFC之列表控件CListCtrl


在MFC程序中列表控件也是使用很频繁的控件，例如windows的资源管理器就可以用列表控件来实现，如下图：
![这里写图片描述](http://img.blog.csdn.net/20171029194504658?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
列表控件具有以下四种视图：

>  1. 大图标
>  2.  小图标
>  3.  列表
>  4.  详细信息
## 1. 新建项目
新建一个基于对话框项目“day13”，布置界面如下，从左侧“工具箱”拖动一个List control到界面，再加上两个按钮及Combo Box，如图：
![这里写图片描述](http://img.blog.csdn.net/20171029195344235?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

| 控件名 | 控件ID| 
| --------   |  -----:  |
| List control| IDC_LIST_VIEW| 
| Combo Box    |   IDC_COMBO2|
| 添加行      |   IDC_BUTTON_ADD  |  
| 删除行      |   IDC_BUTTON_DEL   | 

## 2. 添加列表控件变量
单击选中列表控件，右击选择->“添加变量”，添加变量名为m_list,如下：
![这里写图片描述](http://img.blog.csdn.net/20171029195933714?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3. 初始化列表控件
切换到对话框的初始化函数（OnInitDialog()），我们来给列表控件增加三列，
![这里写图片描述](http://img.blog.csdn.net/20171029200613135?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

```
	m_list.ModifyStyle(LVS_TYPEMASK, LVS_REPORT); //设置列表控件样式为详细信息
	m_list.InsertColumn(0,_T("第一列"),LVCFMT_LEFT,120);
	m_list.InsertColumn(1,_T("第二列"),LVCFMT_LEFT,120);
	m_list.InsertColumn(2,_T("第三列"),LVCFMT_LEFT,120);
```
## 4. 添加列表图标
自行下载或者制作两个bmp图标，分别为16*16，和32*32；将图标复制到项目的res资源目录中，![这里写图片描述](http://img.blog.csdn.net/20171029201802886?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
切换到资源视图，右击添加资源，导入我们准备好的图标，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171029201954651?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
导入好之后我们可以更改位图ID，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171029202051457?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
接下来我们在day13.h的头文件中添加两个成员变量：

```
	CImageList m_ilLarge;
	CImageList m_ilSmall; 
```
分别来对应32*32，和16*16；
然后我们再切换到初始化函数中，添加如下四行代码：

```
	m_ilLarge.Create(IDB_BITMAP_32, 32, 1,RGB(255,0,255));
	m_ilSmall.Create(IDB_BITMAP_16, 16, 1,RGB(255,0,255));

	m_list.SetImageList(&m_ilLarge,LVSIL_NORMAL);
	m_list.SetImageList(&m_ilSmall,LVSIL_SMALL);
```
## 5. 实现添加行按钮函数
双击“添加行”按钮，编辑按钮点击方法：

```
void Cday13Dlg::OnBnClickedButtonAdd()
{
	// TODO: 在此添加控件通知处理程序代码
	int nCount = m_list.GetItemCount();
	CString strText;
	strText.Format(_T("第%d行，第一列"), nCount + 1);
	m_list.InsertItem(nCount,strText,0);
	strText.Format(_T("第%d行，第二列"), nCount + 1);
	m_list.SetItemText(nCount,1,strText);
	strText.Format(_T("第%d行，第三列"), nCount + 1);
	m_list.SetItemText(nCount,2,strText);
}
```
注意，只有添加第一行第一个元素是才是InsertItem，之后的添加都应该是SetItemText，防止出错；
## 5. 实现删除行按钮函数
双击“删除行”按钮，编辑按钮点击方法：

```
void Cday13Dlg::OnBnClickedButtonDel()
{
	// TODO: 在此添加控件通知处理程序代码
	int nCount = m_list.GetItemCount();
	for (int i = nCount; i>=0 ; --i)
	{
		if (m_list.GetItemState(i,LVIS_SELECTED) == LVIS_SELECTED)
		{
			m_list.DeleteItem(i);
		}
	}
}
```
这样就实现了删除行的按钮，并且所有被选中的行都会被删除，按住Ctrl选中多行，点击删除，所有被选中的行都会被删除；


## 6. 实现列表控件的样式切换
切换到资源视图，单击Combo Box，打开属性->data;输入：

> 大图标;小图标;详细信息;列表;

如图：
![这里写图片描述](http://img.blog.csdn.net/20171029205119435?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

继续编辑Combo Box的属性，选择“控件事件”，添加CBN_Selchange事件，如图：
![这里写图片描述](http://img.blog.csdn.net/20171029205441857?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
编辑Combo Box的OnCbnSelchangeCombo2处理函数：

```
void Cday13Dlg::OnCbnSelchangeCombo2()
{
	// TODO: 在此添加控件通知处理程序代码
	DWORD dwStyle;
	CComboBox *pView;
	pView = (CComboBox *)GetDlgItem(IDC_COMBO2);
	switch(pView->GetCurSel())
	{
	case 0:
		dwStyle = LVS_ICON;
		break;
	case 1:
		dwStyle = LVS_SMALLICON;
		break;
	case 2:
		dwStyle = LVS_LIST;
		break;
	case 3:
		dwStyle = LVS_REPORT;
		break;
	default:
		return;
	}
	m_list.ModifyStyle(LVS_TYPEMASK,dwStyle);
}
```
很明显，先用GetDlgItem获取Combo Box的对象，然后判断Combo Box的选中的是哪一项，记录选中项的列表类型，最后设置列表属性；
## 最后效果图：
大图标:
![这里写图片描述](http://img.blog.csdn.net/20171029210611657?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
小图标：
![这里写图片描述](http://img.blog.csdn.net/20171029210644041?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

列表：
![这里写图片描述](http://img.blog.csdn.net/20171029210701658?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
详细信息：
![这里写图片描述](http://img.blog.csdn.net/20171029210716406?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)

### [>>>我的私人博客<<<](http://blog.amuuncle.site/)
