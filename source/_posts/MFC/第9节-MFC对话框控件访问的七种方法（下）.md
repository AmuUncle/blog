---
title: 第9节 MFC对话框控件访问的七种方法（下）
date: 2017-10-28 23:33:13
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# Windows编程基础--第9节 MFC对话框控件访问的七种方法（下）

上节学习了MFC访问控件的三种方法，这节我们来学习剩下的四种方法，四种方法分别如下：

> 第四种  
> 把控件和整型变量相关联
> 
> 第五种
> 把控件和控件变量相关联
> 
> 第六种
>  SendMessage方法
> 
> 第七种
> SendDlgItemMessage方法
# 方法四 把控件和整型变量相关联
## 1. 创建项目
打开上节用到的day08项目，切换到资源视图，添加一个按钮“方法4”，我们在此按钮上实现方法四，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171025194222125?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 2. 关联整型变量
单击选择身高的输入框（IDC_EDIT_SG）,右击选择“添加变量”，打开如下界面：
![这里写图片描述](http://img.blog.csdn.net/20171025194458916?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
现在我们先选择类别为“value”，然后选择变量类型选择“int”，变量名“m_Height”，其余的默认就好，不过你也可以尝试修改一下最大值，最小值等。如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171025195031283?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
现在我们切换到解决方案视图，可以看见，**day08Dlg.h**中已经增加了一个类变量，m_Height，**day08Dlg.cpp**中DoDataExchange也增加该变量的关联方法，将变量 m_Height和IDC_EDIT_SG的输入框关联起来，如下：

```
void Cday08Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDIT_SG, m_Height);
}
```
还有day08Dlg的构造函数中也对m_Height进行了初始化，如下：

```
Cday08Dlg::Cday08Dlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(Cday08Dlg::IDD, pParent)
	, m_Height(0)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}
```
我们可以看到m_Height的初始化值为0，现在我们编译运行程序，可以看到身高输入框中的值就为0，如图：
![这里写图片描述](http://img.blog.csdn.net/20171025195934143?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
接下来我们分别关联IDC_EDIT_TZ和IDC_EDIT_BMI为变量int m_Weight,double m_BMI;

```
	int m_Height;
	int m_Weight;
	double m_BMI;
```

## 3.实现按钮事件
现在m_Height ，m_Weight ，m_BMI 分别和界面上的三个输入框相关联，所以我们可以直接取它们的值就可以，也可以直接进行赋值，但这是会用下面这个方法:

> UpdateData(TRUE);   //把控件的值关联到变量 
> UpdateData(FALSE);  //把变量的值关联到控件

```
void Cday08Dlg::OnBnClickedButtonFunc4()
{
	// TODO: 在此添加控件通知处理程序代码
	UpdateData(TRUE);   //把控件的值关联到变量
	double dHeight = m_Height / 100.00;
	m_BMI = m_Weight / (dHeight * dHeight );
	UpdateData(FALSE);  //把变量的值关联到控件
}
```
编译运行，这时就可以看到点击方法4之后，BMI值就计算出来了，如图：
![这里写图片描述](http://img.blog.csdn.net/20171025201108120?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
# 方法五 把控件和控件变量相关联
## 1. 添加“方法5”按钮
如图：
![这里写图片描述](http://img.blog.csdn.net/20171025201519201?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 1. 关联控件变量
单击选择身高的输入框（IDC_EDIT_SG）,右击选择“添加变量”，打开如下界面：
![这里写图片描述](http://img.blog.csdn.net/20171025201559731?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

现在我们先选择类别为“control”，变量名“m_edit_Height”，其余的默认就好，不过你也可以尝试修改一下最大值，最小值等。如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171025211636783?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
接下来我们分别关联IDC_EDIT_TZ和IDC_EDIT_BMI为变量	CEdit m_edit_tz, CEdit m_edit_bmi;
```
	CEdit m_edit_sg;
	CEdit m_edit_tz;
	CEdit m_edit_bmi;
```
## 3.实现按钮事件
现在m_edit_sg，m_edit_tz，m_edit_bmi分别和界面上的三个输入框相关联，所以我们可以直接取它们的值就可以，也可以直接进行赋值，但这是会用下面这个方法:

```
void Cday08Dlg::OnBnClickedButtonFunc5()
{
	// TODO: 在此添加控件通知处理程序代码
	TCHAR tcHeight[10], tcWeight[10] , tcBMI[10];
	m_edit_sg.GetWindowText(tcHeight,10);
	m_edit_tz.GetWindowText(tcWeight,10);

	int nHeight = _ttoi(tcHeight);
	double dHeight = nHeight / 100.00;
	int nWeight = _ttoi(tcWeight);

	double bmi = nWeight/(dHeight * dHeight);
	char buf[28];
	sprintf(buf, "%.3f", bmi);
	m_edit_bmi.SetWindowText(buf);
}
```

# 方法六 SendMessage方法
通过SendMessage方法发送WM_GETTEXT消息到控件所在窗口来获取控件文本值，同样发送WM_SETTEXT消息到控件所在窗口来设置控件文本值；
```
void Cday08Dlg::OnBnClickedButtonFunc6()
{
	// TODO: 在此添加控件通知处理程序代码
	TCHAR tcHeight[10], tcWeight[10] , tcBMI[10];
	::SendMessage(GetDlgItem(IDC_EDIT_SG)->m_hWnd,WM_GETTEXT,10,(LPARAM)tcHeight);
	::SendMessage(GetDlgItem(IDC_EDIT_TZ)->m_hWnd,WM_GETTEXT,10,(LPARAM)tcWeight);

	int nHeight = _ttoi(tcHeight);
	double dHeight = nHeight / 100.00;
	int nWeight = _ttoi(tcWeight);

	double bmi = nWeight/(dHeight * dHeight);
	char buf[28];
	sprintf(buf, "%.3f", bmi);
	::SendMessage(GetDlgItem(IDC_EDIT_BMI)->m_hWnd,WM_SETTEXT,10,(LPARAM)buf);
}
```
# 方法七 SendDlgItemMessage方法
通过SendDlgItemMessage方法发送WM_GETTEXT消息到控件所在窗口来获取控件文本值，同样发送WM_SETTEXT消息到控件所在窗口来设置控件文本值；
```
void Cday08Dlg::OnBnClickedButtonFunc7()
{
	// TODO: 在此添加控件通知处理程序代码
	TCHAR tcHeight[10], tcWeight[10] , tcBMI[10];
	SendDlgItemMessage(IDC_EDIT_SG,WM_GETTEXT,10,(LPARAM)tcHeight);
	SendDlgItemMessage(IDC_EDIT_TZ,WM_GETTEXT,10,(LPARAM)tcWeight);

	int nHeight = _ttoi(tcHeight);
	double dHeight = nHeight / 100.00;
	int nWeight = _ttoi(tcWeight);

	double bmi = nWeight/(dHeight * dHeight);
	char buf[28];
	sprintf(buf, "%.3f", bmi);

	SendDlgItemMessage(IDC_EDIT_BMI,WM_SETTEXT,10,(LPARAM)buf);
}
```

总结，以上七种方法虽然结果相同，但是其内部机制是有所区别的，在我们将来的编程中要根据实际情况来选择合适的方法，最后，我们列举一下这七种方法：
| 方法名        | 简介   | 
| --------   | -----:  |
| GetDlgItem()     | 获取控件对象 |
| GetDlgItemText()        |   获取对象文本   |  
| GetDlgItemInt()         |    获取对象整型值   | 
| DDX_Text(pDX,IDC_EDIT_SG, m_Height);        |    把控件和整型变量相关联   | 
| DDX_Control(pDX,IDC_EDIT_BMI,m_edit_bmi);  |    把控件和控件变量相关联    | 
| SendMessage       |    发送WM_GETTEXT消息到控件所在窗口来获取控件文本值   | 
| SendDlgItemMessage         |   发送WM_GETTEXT消息来获取控件文本值    | 

### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)