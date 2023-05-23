---
title: 第15节 MFC之复选框及单选按钮
date: 2017-11-02 23:00:09
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---

# Windows编程基础--第15节 MFC之复选框及单选按钮

## 1. 新建项目
新建一个基于对话框项目“day17”，布局如下，自行处理：
![这里写图片描述](http://img.blog.csdn.net/20171102215604038?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

拖动三个check box和两个radio button到界面上，设置其ID如下：
| 控件名 | 控件ID| 
| --------   |  -----:  |
| 红色| IDC_CHECK_RED| 
| 绿色   |   IDC_CHECK_GREEN|
| 蓝色     |   IDC_CHECK_BLUE|  
| 矩形      |   IDC_RADIO_SQURAE| 
| 圆形|   IDC_RADIO_CIRC| 
执行“工具”->“tab键位置”，确保两个radio button的顺序是连续的，如下图：
![这里写图片描述](http://img.blog.csdn.net/20171102220353696?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171102220403509?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


指定第一个radio button（矩形）的Group的值为true，如图:
![这里写图片描述](http://img.blog.csdn.net/20171102220705649?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 2. 添加关联变量
添加五个控件的变量，如图：
![这里写图片描述](http://img.blog.csdn.net/20171102221631588?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

```
	DDX_Control(pDX, IDC_CHECK_RED, m_chk_red);
	DDX_Control(pDX, IDC_CHECK_GREEN, m_chk_green);
	DDX_Control(pDX, IDC_CHECK_BLUE, m_chk_blue);
	DDX_Control(pDX, IDC_RADIO_SQURAE, m_rd_squ);
	DDX_Control(pDX, IDC_RADIO_CIRC, m_rd_circ);
```
分别添加如上变量；

## 3. 开始写代码吧
现在我们来让程序运行起来时默认选中圆形；
切换到解决方案视图，进入BOOL Cday17Dlg::OnInitDialog()方法：
在末尾return前加入这一行：

```
	// TODO: 在此添加额外的初始化代码
	CheckRadioButton(IDC_RADIO_SQURAE,IDC_RADIO_CIRC,IDC_RADIO_CIRC);

	return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE
```
代码解释：

> 在IDC_RADIO_SQURAE和IDC_RADIO_CIRC之间选中IDC_RADIO_CIRC

## 添加五个控件的事件处理方法
如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171102224705375?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
剩下四个都如上添加好；
编辑“蓝色”按钮的点击方法：

```
void Cday17Dlg::OnBnClickedCheckBlue()
{
	// TODO: 在此添加控件通知处理程序代码
	Invalidate();
}
```
代码解释：

> Invalidate()让对话框重汇对话框；
## 添加擦除背景消息（OnEraseBkgnd）事件
如图添加OnEraseBkgnd消息处理函数：
![这里写图片描述](http://img.blog.csdn.net/20171102225056653?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
编辑OnEraseBkgnd函数：

```
BOOL Cday17Dlg::OnEraseBkgnd(CDC* pDC)
{
	// TODO: 在此添加消息处理程序代码和/或调用默认值
	BOOL bRet = CDialogEx::OnEraseBkgnd(pDC);
	int nRed,nGreen,nBlue;
	nRed = m_chk_red.GetCheck() ? 255 : 0;
	nGreen = m_chk_green.GetCheck() ? 255 : 0;
	nBlue = m_chk_blue.GetCheck() ? 255 : 0;

	COLORREF crFore = RGB(nRed,nGreen,nBlue);
	CBrush brush;
	brush.CreateSolidBrush(crFore);
	CBrush *pOldBrush = pDC->SelectObject(&brush);

	RECT rc = {100, 40, 400, 340};
	if (m_rd_squ.GetCheck())
	{
		pDC->Rectangle(&rc);
	}
	else{
		pDC->Ellipse(&rc);
	}
	pDC->SelectObject(pOldBrush);
	return bRet;
}
```
代码解释：

> 1. 根据颜色按钮的选择状态来选择颜色为255还是0；
> 2. 用三个的颜色来创建一个画刷；
> 3. 保留旧的画刷；
> 4. 创建RECT 对象，即圆形的大小；
> 5. 根据形状的radio button来选择化圆形还是矩形；
> 6. 还原旧的画刷；


## 实现其他按钮
其他按钮就只用调用OnBnClickedCheckBlue()就可以了；

# 最终效果图：
![这里写图片描述](http://img.blog.csdn.net/20171102225829436?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)

### [>>>我的私人博客<<<](http://blog.amuuncle.site/)

