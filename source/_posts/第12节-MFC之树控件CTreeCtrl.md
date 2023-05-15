---
title: 第12节 MFC之树控件CTreeCtrl
date: 2017-10-30 21:42:36
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
> 树形控件（Tree Control）：用来显示一系列项目的层次关系，最典型的例子是显示磁盘上的文件与文件夹。如果有子项目的话，单击树形控件中的项目可以展开或者收缩其子项目。MFC提供了CTreeCtrl类进行支持。

树控件在windows程序中使用相对也是比较多的控件，例如windows资源管理器左边的浏览视图就是个树控件视图：
![这里写图片描述](http://img.blog.csdn.net/20171030202704102?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
今天我们学习一下使用树控件，实现“添加节点”、“删除节点”、“修改节点”；

## 1. 新建项目
新建一个基于对话框项目“day14”，布局如下，自行处理：
![这里写图片描述](http://img.blog.csdn.net/20171030203600767?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

| 控件名 | 控件ID| 
| --------   |  -----:  |
| Tree Control| IDC_TREE_VIEW| 
| 编辑框    |   IDC_EDIT_ADD_MDY|
| 添加节点      |   IDC_BUTTON_ADD|  
| 删除节点      |   IDC_BUTTON_DEL   | 
| 修改节点      |   IDC_BUTTON_MDY   | 

## 2. 设置树控件属性
编辑树控件如下属性：

| 属性|             修改值|             解释 | 
| --------   |--------         |            -----:  |
| Has Buttons| TRUE      |           在父节点旁边显示+或-| 
| Has Lines   |   TRUE   |   在父节点和子节点之间划线| 
| Line At root      |   TRUE   |  在根节点上划线| 
## 3. 添加树控件变量
给树控件添加一个变量“m_tree”，如图：
![这里写图片描述](http://img.blog.csdn.net/20171030204858144?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 4. 实现添加节点按钮函数
双击“添加节点”按钮，编辑按钮点击方法：

```
void Cday14Dlg::OnBnClickedButtonAdd()
{
	// TODO: 在此添加控件通知处理程序代码
	CString strText;
	GetDlgItemText(IDC_EDIT_ADD_MDY,strText);
	if (strText.GetLength() == 0)
	{
		AfxMessageBox(_T("请输入节点名！"));
		return;
	}
	HTREEITEM hItem = m_tree.GetSelectedItem();
	if(hItem == NULL){
		hItem = TVI_ROOT;
	}

	TVINSERTSTRUCT ts ={0};
	ts.hParent = hItem;
	ts.hInsertAfter = TVI_LAST;
	ts.item.pszText = strText.GetBuffer();
	ts.item.mask = TVIF_TEXT;
	HTREEITEM hNewItem = m_tree.InsertItem(&ts);
	m_tree.SelectItem(hNewItem);
	m_tree.EnsureVisible(hNewItem);
}
```
代码解释：

> 1. 先获取文本框中的值，如果值为空，则提示用户输入；
> 2. 获取当前选中的节点，若不存在选中的节点，则获取根节点；
> 3. 创建节点结构体，设置其父节点，插入方式，节点内容，内容可见等；
> 4. 插入新的节点，并且设置节点保证可见；
效果图：
![这里写图片描述](http://img.blog.csdn.net/20171030211143052?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 5. 实现删除节点按钮函数
双击“删除节点”按钮，编辑按钮点击方法：

```
void Cday14Dlg::OnBnClickedButtonDel()
{
	// TODO: 在此添加控件通知处理程序代码
	HTREEITEM hItem = m_tree.GetSelectedItem();
	if(hItem == NULL){
		AfxMessageBox(_T("请选择要删除的节点！"));
		return;
	}

	HTREEITEM hParentItem = m_tree.GetParentItem(hItem);
	m_tree.DeleteItem(hItem);
	m_tree.SelectItem(hParentItem);
}
```
代码解释：

> 1. 获取选中的节点，若没有选中的节点，则提示用户；
> 2. 获取选中节点的父节点
> 3. 删除选中的节点
> 4. 将其父节点设置为选中节点

删除前：
![这里写图片描述](http://img.blog.csdn.net/20171030211100130?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
删除后：
![这里写图片描述](http://img.blog.csdn.net/20171030211117156?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 6. 实现修改节点按钮函数
双击“修改节点”按钮，编辑按钮点击方法：

```
void Cday14Dlg::OnBnClickedButtonMdy()
{
	// TODO: 在此添加控件通知处理程序代码
	HTREEITEM hItem = m_tree.GetSelectedItem();
	if(hItem == NULL){
		AfxMessageBox(_T("请选择要修改的节点！"));
		return;
	}

	CString strText;
	GetDlgItemText(IDC_EDIT_ADD_MDY,strText);
	if (strText.GetLength() == 0)
	{
		AfxMessageBox(_T("请输入新的节点名！"));
		return;
	}
	m_tree.SetItemText(hItem,strText);
}
```
代码解释：

> 1. 获取选中的节点，若没有选中的节点，则提示用户；
> 2. 先获取文本框中的值，如果值为空，则提示用户输入；
> 3.修改文本名
## 7. 映射节点选择消息
我们想实现在点击选择控件是，下方的文本框中自动出现选择节点的文本，那么就要映射节点的选择变化消息：TVN_SELCHANGE，如图添加事件处理函数：
![这里写图片描述](http://img.blog.csdn.net/20171030212609773?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
编辑事件处理函数：

```
void Cday14Dlg::OnTvnSelchangedTreeView(NMHDR *pNMHDR, LRESULT *pResult)
{
	LPNMTREEVIEW pNMTreeView = reinterpret_cast<LPNMTREEVIEW>(pNMHDR);
	// TODO: 在此添加控件通知处理程序代码

	HTREEITEM hItem = m_tree.GetSelectedItem();
	if(hItem != NULL){
		CString strText = m_tree.GetItemText(hItem);
		SetDlgItemText(IDC_EDIT_ADD_MDY, strText);
	}
	*pResult = 0;
}
```
代码解释：

> 1. 获取选中的节点，若不存在，则略过，不处理；
> 2. 获取选中的节点文本，将文本值设置到文本框中；

效果图：
![这里写图片描述](http://img.blog.csdn.net/20171030213448114?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

至此，MFC树控件的简单使用已经结束，其实树控件还有很多属性，比如添加图标，这就到以后的实践中再来学习，附树控件常见属性及方法：
### 1、树形控件的属性

> TVS_EDITLABELS:允许用户进行节点文本的编辑 TVS_HASBUTTONS:节点左侧添加一个按钮
> TVS_HASLINES:父节点与子结点出现连线 TVS_LINESATROOT:子节点与根节点之间出现连线
> TVS_NOTOOLTIPS:结点无动态提示 TVS_SINGLEEXPAND:节点的选中(未选中)t7展开(合拢)同步
> MFC中以两种形式封装树形控件，一种是树形控件CTreeCtrl，另一种是树形视图控件CTreeView。对于一般的要求，比如在对话框中，使用CTreeCtrl比较方便。在使用树形视图控件时，只需要利用成员函数取得其引用，就可以像树形控件一样方便的使用：
> CTreeCtrl& GetTreeCtrl( ) const;
> 调用InsertItem函数能够将节点插入树形控件中，并返回插入的项的HTREEITEM。树形控件的插入工作往往是在对话框的OnInitDialog函数中进行，而对于树形视图控件，则是在OnInitUpdate函数中进行。
> 树形控件中的节点数据可以是文本，也可以是图像。节点中使用的图像是和树形控件的图像列表相对应的。在树形控件中使用图像列表是通过使用SetImageList函数来完成。
> 树形控件能产生通告消息，如: TVN_BEGINDRAG开始拖拽 TVN_ITEMEXPANDED节点被展开或收缩
> 其消息映射使用WM_NOTIFI,如： WM_NOTIFI(TVN_BEGINDRAG,IDC_TREECTRL,OnBeginDrag);

### 2、树形控件TVN_BEGINRDRAG消息的响应

> 与树形控件有关的、常用的结构是TVITEM、TVINSERTSTRUCT 、NMTREEVIEW(NM_TREEVIEW
> )。前两个是用于插入节点时使用，而NMTREEVIEW是与树形控件的通告消息相关的结构。
> 当用鼠标左键拖拽树形控件时，控件会发出TVN_BEGINDRAG通告消息；当用鼠标右键拖拽时，则会发出TVN_BEGINRDRAG通告消息。拖拽树形控件时需要使用到IImageList::BeginDrag函数：
> IImageList::BeginDrag creates a temporary image list that is used for
> dragging. In response to subsequent WM_MOUSEMOVE messages, you can
> move the drag image by using IImageList::DragMove. To end the drag
> operation, you can use IImageList::EndDrag. 
> 通常使用CTreeCtrl::CreateDragImage函数创建一个被拖拽节点的图像并返回一个CImageList指针(注意被拖拽的数据节点必须包含图像，否则返回的CImageList指针为空)，然后利用该指针来调用CImageList::BeginDrag函数。除此之外还需要调用CImageList::DragEnter函数锁定、更新窗口，并在指定的位置显示被拖拽的图像：
> static BOOL PASCAL DragEnter(    CWnd* pWndLock,    CPoint point  );
> If pWndLock is NULL, this function draws the image in the display
> context associated with the desktop window, and coordinates are
> relative to the upper left corner of the screen.
> 注意BeginDrag函数只是在拖拽开始时创建要拖拽的图像，而DragEnter函数则显示该图像。
> 最后调用CWnd::SetCapture函数使后续所有的鼠标输入都发送到当前的CWnd对象而不管鼠标的位置（因为CImageList::DragEnter函数的第一个参数为NULL时表示在与桌面窗口相关的窗口，可以说就是当前程序的框架窗口，但不包括其他应用程序的窗口上显示被拖拽的图像。因此要使得被拖拽的图像在所有的窗口上而不仅仅是应用程序的框架窗口上显示，就需要调用CWnd::SetCapture函数。一旦调用了SetCapture函数，则在当前应用程序的非框架窗口，包括系统菜单上的鼠标按键动作均被发送到当前CWnd
> 对象，直到调用ReleaseCapture为止）。
> 然后就是在鼠标移动的消息响应函数中调用CImageList::DragMove函数移动被拖拽的图像，使之与鼠标的移动位置同步。最后是调用CImageList::DragShowNolock函数隐藏或显示拖拽的图像，但它并不是必须的，也可以不调用，因此之前已经调用过CImageList::DragEnter函数显示拖拽的图像了。当传递true值显示拖拽的图像时，DragShowNolock在这个过程中不像DragEnter函数一样锁定窗口。
> 值得注意的是，在拖拽节点过程中可以使用CTreeCtrl::HitTest函数判断鼠标滑动过程中所经过的点是否位于树形控件的某一个节点之上，如果是，则返回该树形节点的HTREEITEM。此时可以使用CTreeCtrl::SelectDropTarget函数或CTreeCtrl::SelectItem函数来高亮显示该节点。

### 3、树形控件的成员函数

> InsertItem函数插入一个节点，并返回新插入的节点的HTREEITEM。
> ItemHasChildren函数根据给定的HTREEITEM判断该节点是否存在子节点。
> GetChildItem函数根据给定的HTREEITEM获取该节点下子节点的HTREEITEM，如果没有子节点，则返回NULL。
> GetNextSiblingItem函数根据给定的HTREEITEM获取该节点的下一个同级节点。
> EnsureVisible函数在必要的时候滚动视图列表控件使得其至少部分可见。需要注意的是，在使用TVE_COLLAPSE调用Expand收缩树形控件后不能再调用该函数，否则收缩操作将无效。

# 感伤：WE输了，RNG输了，心碎了。。。

### [项目源码可以访问我的码云](https://gitee.com/AmuUncle/MFC_CSDN.git)

### [>>>我的私人博客<<<](http://blog.amuuncle.site/)

