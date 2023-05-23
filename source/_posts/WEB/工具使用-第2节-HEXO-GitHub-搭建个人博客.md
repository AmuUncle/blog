---
title: 工具使用--第2节 HEXO+GitHub 搭建个人博客
date: 2017-10-29 14:10:26
type: "tags"
categories: GitHub
tags: HEXO
---
今天突然想搭建一个自己的私人博客，但是又不想为此买一台服务器，所以百度了一下，发现可以利用**HEXO+码云 **搭建私人博客，所以就写篇教程，记录一下吧。

# 1、环境安装配置
## 1.1 安装node
下载地址：https://nodejs.org/en/download/
默认安装就好。

## 1.2 安装git
msysgit是Windows版的Git，从https://git-for-windows.github.io下载（百度一下也有很多下载链接），然后按默认选项安装即可。msysgit的操作命令和Linux基本一致，很多命令是通用的，例如ls，mv，rm等； 
mygit安装完成后，在开始菜单里找到“Git”->“Git Bash”，蹦出一个类似命令行窗口的东西，就说明Git安装成功！（详情可参见 [ 第1节](http://blog.csdn.net/qq_25549309/article/details/78336107)  ）

## 1.3 申请GitHub账号
 打开https://github.com/，自行申请账号；
![这里写图片描述](http://img.blog.csdn.net/20171029125209685?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 1.4 安装HEXO　
切换到命令行工具，CMD输入命令安装：
> npm install -g hexo

等待安装完成；不过国内NPM镜像速度极慢，可以安装淘宝的cnpm；

> npm install -g cnpm --registry=https://registry.npm.taobao.org

![这里写图片描述](http://img.blog.csdn.net/20171027223208790?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
然后使用cnpm来下载HEXO，如下：

> cnpm install -g hexo

![这里写图片描述](http://img.blog.csdn.net/20171027223329242?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 1.5 配置HEXO　
切换CMD到你希望创建博客项目的目录，然后输入hexo init来初始化一个项目，如：

> cd c:/workspase/blog
> hexo init

继续输入命令：
> hexo generate 或者 hexo g

![这里写图片描述](http://img.blog.csdn.net/20171027224238089?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
生成静态页面

## 1.6 启动本地服务

> hexo server

![这里写图片描述](http://img.blog.csdn.net/20171027224320127?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
可以看到提示Hexo已经运行在http://localhost:4000/上，我们用浏览器打开 http://localhost:4000/看看效果：
![这里写图片描述](http://img.blog.csdn.net/20171027224449843?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

神奇的博客界面就出现了；

# 2、配合Github搭建个人博客
## 2.1 登录Github创建一个项目
1. 登录Github，点击上方的添加项目：我们来添加一个GIT版本仓，点击+号，选择“New repository”，如图：
![这里写图片描述](http://img.blog.csdn.net/20171029125325008?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
2. 打开创建对话框之后，输入repository名，*****.github.io，星号代表你的用户名，记住结尾一定要用.github.io结尾，如果你输入的格式或者用户名不匹配，最后创建的网站可能加载不出css，js等资源，具体原因还没弄清，待以后验证，暂时就按照规范来，如图：
![这里写图片描述](http://img.blog.csdn.net/20171029125935968?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
其余的默认就好，点击“Create repository”来创建仓库；（我的由于已经创建同名的，所以弹出提示，请无视）
3. 创建好之后进入创建好的界面，如下：
![这里写图片描述](http://img.blog.csdn.net/20171029130258224?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
由于我的已经上传过文件，所以你们是没有红框中的内容，不急，接下来我们来看怎么上传文件；
4. 本地mygit还需要配置ssh秘钥，邮箱等才能和github进行上传，修改等操作；
这一步如果没设置过，参见[工具使用--第1节 git使用简记](http://blog.csdn.net/qq_25549309/article/details/78336107)
## 2.2 关联Github和HEXO
1. 进入我们在 **1.5 配置HEXO** 创建的HEXO项目目录，打开根目录中的**_config.yml**文件（以记事本文件打开）；在文件最末尾添加如下三行：
![这里写图片描述](http://img.blog.csdn.net/20171029130914657?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
将其中的repo改为你自己repository地址，你的repository地址在github界面的这里获取，
如图：
![这里写图片描述](http://img.blog.csdn.net/20171029131626085?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
点击“2”处就可以直接复制地址,最后添加的三条就是：

```
deploy:
  type: git
  repo: https://github.com/AmuUncle/AmuUncle.github.io.git
  branch: master
```
**注意：**每项的冒号后都要留一个英文的空格号；
2. 在HEXO项目根目录中右击选择“Git Bash Here”
![这里写图片描述](http://img.blog.csdn.net/20171029132100372?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
3. 生成静态网站并同步到github
执行下面两个命令：

> hexo g   // 生成 
> hexo d   // 同步
或者直接用：
> hexo d -g  // 在同步前先生成网站

中间可能会让你输入github的账号密码，输入就好：
运行结果如下：
![这里写图片描述](http://img.blog.csdn.net/20171029132536364?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
这样网站就同步到github中了；我们可以刷新github页面。可以看到已经有很多文件了：
![这里写图片描述](http://img.blog.csdn.net/20171029132712757?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## 2.3 让网站显示出来
我们点击github界面上的Settings按钮，进入设置界面：
![这里写图片描述](http://img.blog.csdn.net/20171029132847207?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
往下拖动，找到“github pages”选项，点击“Launch Automatic page generator”按钮，开启**github pages**功能；
![这里写图片描述](http://img.blog.csdn.net/20171029133016297?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
这时我们就可已输入“https://AmuUncle.github.io”来打开我们创建的blog网站；
如下：
![这里写图片描述](http://img.blog.csdn.net/20171029133449652?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
至此，我们已经成功将网站部署到GITHUB，并且是个人独立博客哦。。。

# 3、设置HEXO的主题
这里网上很多教程，很简单，很多人推荐NEXT主题，我也用的是这款，功能很齐全，这里我就直接给教程链接了，很详细；

> NEXT主题官网，教程非常详细：http://theme-next.iissnan.com/getting-started.html
> HEXO主题类列表：https://hexo.io/themes/

其他主题也差不多配置方法，自己研究吧。。
# 4、将域名和github博客地址关联（个人需求）
4.1 购买域名
我是在阿里云购买的.site域名,很便宜，一年才几块钱，有需要的可以去看看：

> https://wanwang.aliyun.com/domain/?spm=5176.8076989.763973.3.5a54fa45x7NU0Z

![这里写图片描述](http://img.blog.csdn.net/20171029134437343?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

4.2 配置域名
进入域名解析配置界面，添加一下三项：
![这里写图片描述](http://img.blog.csdn.net/20171029134722933?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
解析列表：
| 方法记录类型 | 主机记录| 记录值 |
| --------   |  --------   | -----:  |
| CNAME     | www | AmuUncle.github.io |
| A       |   @   |   192.30.252.154 |  
| A       |   @   |   192.30.252.153 |  

其中 192.30.252.153和 192.30.252.154 为github的IP地址；
域名这边已经配置好，但还没结束，我们再来到HEXO博客的目录，进入source目录，新建一个CNAME文件，没有任何后缀名，编辑内容为：`amuuncle.site`
![这里写图片描述](http://img.blog.csdn.net/20171029135626125?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20171029135635278?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

接下来输入：

> hexo d -g

重新生成同步网站到github，接下来就是见证奇迹的时候我们到浏览器输入我们的域名，就打开了我们的blog页面，如图（如果打不开，请等待10分钟，因为更改域名解析要十分钟后才能生效）
![这里写图片描述](http://img.blog.csdn.net/20171029140306025?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
最终效果图，完美，接下来我们就可以自由写个人微博，并且部署到github了，配置好域名之后，不注意根本发现不了你是在github上部署的网站哦。
使用如下命令添加一篇博客，然后进入项目的source\_posts目录找打创建的md文件，编辑此文件就是在写博客；
> hexo new post "工具使用--第2节 HEXO+GitHub 搭建个人博客"

对于md文件的编写，网上有很对教程，我使用的工具是：**Haroopad**，完全没费，可自行下载。
![这里写图片描述](http://img.blog.csdn.net/20171029141421963?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
记住写完之后还是要输入：
> hexo d -g

来重新生成同步网站到github；

最后，我的blog地址就是[>>>我的私人博客<<<](http://blog.amuuncle.site/)
欢饮大家光临指教。