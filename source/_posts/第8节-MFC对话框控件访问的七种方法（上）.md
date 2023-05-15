---
title: 第8节 MFC对话框控件访问的七种方法（上）
date: 2017-10-28 23:32:43
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# Windows编程基础--第8节 MFC对话框控件访问的七种方法（上）

MFC对话框控件具有以下三种访问方式(当然还有很多别的访问方式，今天时间紧急，先学这三种)，分别是：
> 第一种
> GetDlgItem()->GetWindowText()
> GetDlgItem()->SetWindowText()
> 
> 第二种
> GetDlgItemText()

> 第三种
> GetDlgItemInt()
> SetDlgItemInt()

### 1.新建一个对话框项目
参见上节，我们这节采用VS2010编写一个身高体重计算器（BMI），参见 [第二节](http://blog.csdn.net/qq_25549309/article/details/78277801)；

### 2.布局
编辑布局如下：
![这里写图片描述](http://img.blog.csdn.net/20171024220008701?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

| EDIT名称        | ID		| 
| --------   | -----:  |
| 身高     | IDC_EDIT_SG |
| 体重        |   IDC_EDIT_TZ   | 
| BMI        |   IDC_EDIT_BMI   | 

### 3.实现方法
双击确认按钮，编辑其点击消息处理函数；

```
void Cday08Dlg::OnBnClickedOk()
{
	// TODO: 在此添加控件通知处理程序代码
	int nHeight= GetDlgItemInt(IDC_EDIT_SG,NULL,TRUE);
	double dHeight = nHeight / 100.00;
	int nWeight = GetDlgItemInt(IDC_EDIT_TZ,NULL,TRUE);
	double bmi = nWeight/(dHeight*dHeight);
	char buf[28];
	sprintf(buf, "%.3f", bmi);
	SetDlgItemText(IDC_EDIT_BMI,buf);
}
```
这里可以看见使用到了GetDlgItemInt，这就是直接获取文本框的值，并返回为整形，然后用sprintf(buf, "%.3f", bmi);将double类型值转换成字符串，并通过SetDlgItemText将字符串的值设置到ID为IDC_EDIT_BMI的文本框上；
### 4.编译运行
估计很多人会像我一样，VS2010会报这样的错误：
![这里写图片描述](http://img.blog.csdn.net/20171024221112999?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
这是因为我们创建的项目的字符集为Unicode，不允许这样转换，这时我们只要将解决方案中右击项目名“day09”->“属性”->“配置属性”->"常规"->"字符集"->选择“使用多字节字符集”就好了，如下:
![这里写图片描述](http://img.blog.csdn.net/20171024221553536?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171024221603771?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
这时就可以通过编译，运行结果如下：
![这里写图片描述](http://img.blog.csdn.net/20171024221658382?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 5.其他方法
再次编辑“确认”按钮的点击消息处理函数；
**第二种**
```
void Cday08Dlg::OnBnClickedOk()
{
	// TODO: 在此添加控件通知处理程序代码
	TCHAR tcHeight[10], tcWeight[10];
	GetDlgItem(IDC_EDIT_SG)->GetWindowText(tcHeight,10);
	GetDlgItem(IDC_EDIT_TZ)->GetWindowText(tcWeight,10);

	int nHeight = _ttoi(tcHeight);
	double dHeight = nHeight / 100.00;
	int nWeight = _ttoi(tcWeight);
	
	double bmi = nWeight/(dHeight * dHeight);
	char buf[28];
	sprintf(buf, "%.3f", bmi);
	GetDlgItem(IDC_EDIT_BMI)->SetWindowText(buf);
}
```
可以看见，这里用到了GetDlgItem(IDC_EDIT_SG)->GetWindowText(tcHeight,10)方法，这个方法的过程就是先通过GetDlgItem(IDC_EDIT_SG)获取到控件对象，然后调用控件的GetWindowText(tcHeight,10)方法来获取控件的显示文本；

**第三种**
```
void Cday08Dlg::OnBnClickedOk()
{
	TCHAR tcHeight[10], tcWeight[10] , tcBMI[10];
	GetDlgItemText(IDC_EDIT_SG,tcHeight,10);
	GetDlgItemText(IDC_EDIT_TZ,tcWeight,10);

	int nHeight = _ttoi(tcHeight);
	double dHeight = nHeight / 100.00;
	int nWeight = _ttoi(tcWeight);
	
	double bmi = nWeight/(dHeight * dHeight);
	char buf[28];
	sprintf(buf, "%.3f", bmi);
	SetDlgItemText(IDC_EDIT_BMI,buf);
}
```
可以看见，这里直接用到了GetDlgItemText(IDC_EDIT_SG,tcHeight,10)方法，这个方法的过程就是先通过GetDlgItem(IDC_EDIT_SG)获取到控件对象，然后调用控件的GetWindowText(tcHeight,10)方法来设置控件的显示文本；

*虽然上面三种方法最终结果是一样的，但是其本质还是有所区别的*


### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)
