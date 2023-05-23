---
title: 第5节 MFC对话框程序
date: 2017-10-28 23:31:35
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# Windows编程基础--第5节 MFC对话框程序
## 模式对话框
------
对话框程序是MFC最重要的组成部分，也是Visual C++中唯一可以可视化设计的窗口程序，对话框主要有两类：
> * 模式对话框：必须关闭这个对话框才能继续操作父窗口或者上一级窗口
> * 非模式对话框:不影响父窗口或者上一级窗口，可继续操作父窗口或者上一级窗口，对话框程序也可以一直保留，无需关闭才能执行下一步；

接来下我们先一起学习模式对话框；
### 1. 新建项目
建立一个MFC的主对话框项目day04，参见上节，添加两个按钮，分别为“关于”，“聊天”，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171021224403317?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 2. 添加关于对话框
在资源视图（ResourceView）中Dialog上右击->Insert Diallog，插入对话框，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171021225345643?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171021225356308?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 3. 添加关于对话框类
单击添加的关于对话框，执行View->Class Wizard，或者使用快捷键Ctrl + W打开类向导；
由于新的对话框不存在关联类，此时会提示创建一个与它相关联的类，选择Create a new class,单击OK创建关联类，如下图所示：
![这里写图片描述](http://img.blog.csdn.net/20171021225816356?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171021225906889?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
单击OK完成创建关联类；
![这里写图片描述](http://img.blog.csdn.net/20171021230017929?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 3. 添加关于按钮消息事件
切换回主对话框，单击主对话框，执行View->Class Wizard，或者使用快捷键Ctrl + W打开类向导；选择关于按钮，增加clicked方法，然后Edit Code编辑关于按钮的响应方法，或者可以直接双击“关于”按钮就可以直接进入按钮点击方法，在day04Dlg.h中添加“#include AboutDlg.h”来引入对话框类，然后我们来编辑关于按键方法，创建一个模式对话框；

```
void CDay04Dlg::OnButtonAbout() 
{
	// TODO: Add your control notification handler code here
	CAboutDlg dlg;
	dlg.DoModal();
}
```
效果图：
![这里写图片描述](http://img.blog.csdn.net/20171021231034007?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
至此，一个模式对话框就创建成功了，我们可以看到，我们必须关闭关于对话框，才能单击主对话框。


## 非模式对话框

现在我们来创建一个非模式对话框；
### 1. 添加聊天对话框
在资源视图（ResourceView）中Dialog上右击->Insert Diallog，插入对话框，如图所示：
![这里写图片描述](http://img.blog.csdn.net/20171021231642278?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 2. 添加聊天对话框类
单击添加的关于对话框，执行View->Class Wizard，或者使用快捷键Ctrl + W打开类向导；
由于新的对话框不存在关联类，此时会提示创建一个与它相关联的类，选择Create a new class,单击OK创建关联类，如上面步骤3
### 3. 添加聊天按钮消息事件
切换回主对话框，单击主对话框，执行View->Class Wizard，或者使用快捷键Ctrl + W打开类向导；选择聊天按钮，增加clicked方法，然后Edit Code编辑关于按钮的响应方法，或者可以直接双击“聊天”按钮就可以直接进入按钮点击方法，在day04Dlg.h中添加“#include "Chat.h"”来引入对话框类，然后我们来编辑聊天按键方法，创建一个非模式对话框；

```
void CDay04Dlg::OnButtonChat() 
{
	// TODO: Add your control notification handler code here
	CChat * pDlg = new CChat;
	pDlg->Create(IDD_DIALOG_CHAT);
	pDlg->ShowWindow(SW_SHOW);
}
```
效果图：
![这里写图片描述](http://img.blog.csdn.net/20171021232153087?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171021232202529?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
至此，一个非模式对话框就创建成功了，我们可以看到，我们打开聊天界面后还可以继续操作父窗口中的关于对话框，甚至还可以单击聊天对话框创建多个聊天界面；
![这里写图片描述](http://img.blog.csdn.net/20171021232914420?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)