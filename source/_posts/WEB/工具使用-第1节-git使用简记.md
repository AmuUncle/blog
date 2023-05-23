---
title: 工具使用--第1节 git使用简记
date: 2017-10-28 23:38:48
type: "tags"
categories: git教程
tags: GIT
---
# 工具使用--第1节 git使用简记

## GIT （分布式版本控制系统） 

> Git是一款免费、开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。  Git的读音为/gɪt/。 Git是一个开源的分布式版本控制系统，可以有效、高速的处理从很小到非常大的项目版本管理。 Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。 Torvalds 开始着手开发 Git 是为了作为一种过渡方案来替代 BitKeeper，后者之前一直是 Linux 内核开发人员在全球使用的主要源代码工具。开放源码社区中的有些人觉得BitKeeper 的许可证并不适合开放源码社区的工作，因此 Torvalds 决定着手研究许可证更为灵活的版本控制系统。尽管最初 Git 的开发是为了辅助 Linux 内核开发的过程，但是我们已经发现在很多其他自由软件项目中也使用了 Git。例如 很多 Freedesktop 的项目迁移到了Git 上。    --- **百度百科**

## 1.安装git
这里只说windows版本安装使用，Linux版本等以后再研究；
### 1.1  下载msysgit
**msysgit**是Windows版的Git，从https://git-for-windows.github.io下载（百度一下也有很多下载链接），然后按默认选项安装即可。**msysgit**的操作命令和Linux基本一致，很多命令是通用的，例如ls，mv，rm等；
mygit安装完成后，在开始菜单里找到“Git”->“Git Bash”，蹦出一个类似命令行窗口的东西，就说明Git安装成功！

## 2. 配置msysgit
在桌面空白处右击，选择“Git Bash here”进入msysgit的控制台，输入一下两条命令，配置全局的用户名和邮箱：
```
$ git config --global user.name "你的用户名"
$ git config --global user.email "邮箱地址"
```
你的用户名：可以随意设置，但要记住用户名
邮箱地址：你的邮箱地址

## 3.创建代码仓
### 3.1 进入你想建仓的目录
在目录空白处右击选择“Git Bash here”进入msysgit的控制台，输入git init命令把这个目录变成Git可以管理的仓库：

> $ git init
>  Initialized empty Git repository in C:/Users/Administrator/Desktop/usb_encryption_5.4.0/git_demo/.git/

git会在此目录创建.git目录，这是Git来跟踪管理版本库的，无需我们来改动，

## 4.版本控制
我们现在在此目录下来创建一个readme.md文件，随意填写些内容，如下
![这里写图片描述](http://img.blog.csdn.net/20171024232855549?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 4.1 查看版本状态

> git status
![这里写图片描述](http://img.blog.csdn.net/20171024233234409?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 4.2 添加到缓存区

```
git add readme.md
```
![这里写图片描述](http://img.blog.csdn.net/20171024233414198?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 4.3 提交代码到版本仓

```
 git commit -m "Add readme"
```
![这里写图片描述](http://img.blog.csdn.net/20171024233600207?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

-m 后面跟得是你提交的代码的描述，建议所有提交都应该添加描述。


*暂时先记录这么多，下次再补充完整*
