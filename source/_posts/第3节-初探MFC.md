---
title: 第3节 初探MFC
date: 2017-10-28 23:14:58
type: "tags"
categories: MFC从入门到放弃
tags: MFC
---
# Windows编程基础--第3节 初探MFC
 1. 前言
	 win32程序属于早期windows软件，已经逐渐被淘汰，但它的设计模式和方法大部分都被MFC所继承，并且MFC开始使用C++语言进行开发，借助C++比C语言的强大特性，使得开发windws程序更加简便、高效，更加多元化。
 2. 创建第一个MFC程序（操作系统：win10 64位 IDE：vc++ 6.0） 
 1)  执行File->new，选择Project选项卡，选择下面的MFC AppWizard，填写项目名称等，如图：
 ![这里写图片描述](http://img.blog.csdn.net/20171019213728124?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 2）点击 OK 按钮进入下一页，我们先选择简单的Dialog based，然后->NEXT ，第三页进行是否选择MFC静态库还是共享库等选择，这里我们不作修改，直接点击Finish，完成创建；
 ![这里写图片描述](http://img.blog.csdn.net/20171019214152011?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 
 3）现在可以尝试编译，运行打开默认的Dialog界面
 ![这里写图片描述](http://img.blog.csdn.net/20171019214358362?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 4)现在我们往刚才创建的Dialog中添加一些资源控件，如下图：
 ![这里写图片描述](http://img.blog.csdn.net/20171019221812073?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 注意：ListCtrl属性中Stytle->View选择Report
 5）
 接下来我们来实现底部三个按钮的方法：
	添加按钮
```
 void CDay02Dlg::OnAdd() 
{
	// TODO: Add your control notification handler code here
	CString szNumb,szName,szSala;
	GetDlgItemText(IDC_NUMB,szNumb);
	GetDlgItemText(IDC_NAME,szName);
	GetDlgItemText(IDC_SALA,szSala);
	CListCtrl *pList = (CListCtrl*)GetDlgItem(IDC_LIST);
	int nCount = pList->GetItemCount();
	pList->InsertItem(nCount,szNumb);
	pList->SetItemText(nCount,1,szName);
	pList->SetItemText(nCount,2,szSala);
}
```
先通过GetDlgItemText方法获取顶部三个Edit输入的参数值，并分别赋值给szNumb,szName,szSala;
接下来通过GetDlgItem取得ListCtrl的操作句柄，获取ListCtrl当前总数，在末尾添加一个Iten，并赋值；
	
	删除按钮
```
void CDay02Dlg::OnDel() 
{
	// TODO: Add your control notification handler code here
	CListCtrl *pList = (CListCtrl*)GetDlgItem(IDC_LIST);
	int nSel = pList->GetSelectionMark();
	if(nSel < 0)
	{
		AfxMessageBox("请先选择要删除的员工");
		return;
	}
	pList->DeleteItem(nSel);
}
```
获取ListCtrl的操作句柄后获取到当前选的行数，最后删除改行；

修改按钮：

```
void CDay02Dlg::OnMod() 
{
	// TODO: Add your control notification handler code here
	CListCtrl *pList = (CListCtrl*)GetDlgItem(IDC_LIST);
	int nSel = pList->GetSelectionMark();
	if(nSel < 0)
	{
		AfxMessageBox("请先选择要修改的员工");
		return;

	}	
	CString szNumb,szName,szSala;
	GetDlgItemText(IDC_NUMB,szNumb);
	GetDlgItemText(IDC_NAME,szName);
	GetDlgItemText(IDC_SALA,szSala);
	pList->SetItemText(nSel,0,szNumb);
	pList->SetItemText(nSel,1,szName);
	pList->SetItemText(nSel,2,szSala);
	
}
```
先通过GetDlgItemText方法获取顶部三个Edit输入的参数值，并分别赋值给szNumb,szName,szSala;
接下来通过GetDlgItem取得ListCtrl的操作句柄，获取ListCtrl当前选择行数，将获取的szNumb,szName,szSala分别赋值给当前Item的对应位置；



函数原型如下：
BOOL SetItemText( int nItem, int nSubItem, LPTSTR lpszText );用于MFC设置CListCtrl控件中的列表项内容。

int GetDlgItemText( int nID, CString& rString) 
 nID 指定了要获取其标题的控件的整数标识符。 lpStr 指向要接收控件的标题或文本的缓冲区。 nMaxCount 指定了要拷贝到lpStr的字符串的最大长度（以字节为单位）。如果字符串比nMaxCount要长，它将被截断。 rString 对一个CString对象的引用。

 3.最终效果图
 ![这里写图片描述](http://img.blog.csdn.net/20171019223448248?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
4. day02.cpp 源码

```
	// day02Dlg.cpp : implementation file
//

#include "stdafx.h"
#include "day02.h"
#include "day02Dlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CAboutDlg dialog used for App About

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	//{{AFX_MSG(CAboutDlg)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// No message handlers
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CDay02Dlg dialog

CDay02Dlg::CDay02Dlg(CWnd* pParent /*=NULL*/)
	: CDialog(CDay02Dlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CDay02Dlg)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CDay02Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CDay02Dlg)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CDay02Dlg, CDialog)
	//{{AFX_MSG_MAP(CDay02Dlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON4, OnButtonOK)
	ON_BN_CLICKED(IDC_ADD, OnAdd)
	ON_BN_CLICKED(IDC_DEL, OnDel)
	ON_BN_CLICKED(IDC_MOD, OnMod)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CDay02Dlg message handlers

BOOL CDay02Dlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	CListCtrl *pList = (CListCtrl*)GetDlgItem(IDC_LIST);
	pList->InsertColumn(0,"学号",0,100);
	pList->InsertColumn(1,"姓名",0,100);
	pList->InsertColumn(2,"工资",0,100);

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	// TODO: Add extra initialization here
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CDay02Dlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CDay02Dlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CDay02Dlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CDay02Dlg::OnButtonOK() 
{
	// TODO: Add your control notification handler code here
	
}

void CDay02Dlg::OnAdd() 
{
	// TODO: Add your control notification handler code here
	CString szNumb,szName,szSala;
	GetDlgItemText(IDC_NUMB,szNumb);
	GetDlgItemText(IDC_NAME,szName);
	GetDlgItemText(IDC_SALA,szSala);
	CListCtrl *pList = (CListCtrl*)GetDlgItem(IDC_LIST);
	int nCount = pList->GetItemCount();
	pList->InsertItem(nCount,szNumb);
	pList->SetItemText(nCount,1,szName);
	pList->SetItemText(nCount,2,szSala);
}

void CDay02Dlg::OnDel() 
{
	// TODO: Add your control notification handler code here
	CListCtrl *pList = (CListCtrl*)GetDlgItem(IDC_LIST);
	int nSel = pList->GetSelectionMark();
	if(nSel < 0)
	{
		AfxMessageBox("请先选择要删除的员工");
		return;

	}
	pList->DeleteItem(nSel);

	
}

void CDay02Dlg::OnMod() 
{
	// TODO: Add your control notification handler code here
	CListCtrl *pList = (CListCtrl*)GetDlgItem(IDC_LIST);
	int nSel = pList->GetSelectionMark();
	if(nSel < 0)
	{
		AfxMessageBox("请先选择要修改的员工");
		return;

	}	
	CString szNumb,szName,szSala;
	GetDlgItemText(IDC_NUMB,szNumb);
	GetDlgItemText(IDC_NAME,szName);
	GetDlgItemText(IDC_SALA,szSala);
	pList->SetItemText(nSel,0,szNumb);
	pList->SetItemText(nSel,1,szName);
	pList->SetItemText(nSel,2,szSala);
	
}
```

项目源码可以访问我的码云来fork：

```
https://gitee.com/AmuUncle/MFC_CSDN.git
```