---
title: python selenium 自动化查询上海公交卡余额，并邮件通知
date: 2017-10-29 00:49:43
type: "tags"
categories: PYTHON实战
tags: PYTHON
password: password
---

# python selenium 自动化查询上海公交卡余额，并邮件通知
1、下载python安装。
　　https://www.python.org/downloads/release/python-351/
2、安装selenium
2.1、通过pip 安装
	pip install selenium
	 
2.2、通过下载包安装 ,直接下载selenium包：
	https://pypi.python.org/pypi/selenium
    解压，cmd进入目录:
		 python setup.py install
		 
3 、 安装Chrome driver
	下载地址：http://npm.taobao.org/mirrors/chromedriver
	下载解压，将 chromedriver.exe 文件放到chrome的安装目录下...\Google\Chrome\Application\ ,然后设置path环境变量；
	![chromedriver与chrome各版本对应表](http://img.blog.csdn.net/20171016220018549?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjU1NDkzMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

4、全部代码

```
	# coding = utf-8

from selenium import webdriver
from time import sleep
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
cardIDList = [u"u54311******", u"u728833******"]


def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):
    '''
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收信人的邮箱地址
    @fromaddr:发信人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱密码
    '''
    mail_msg = MIMEMultipart()
    mail_msg['Subject'] = subject
    mail_msg['From'] =fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))
    try:
        s = smtplib.SMTP()
        s.connect(smtpaddr)  #连接smtp服务器
        s.login(fromaddr,password)  #登录邮箱
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #发送邮件
        s.quit()
    except :
       print ("Error: unable to send email")
       print (traceback.format_exc())


def get_gj_info(cardID):
    for i in range(1, 10, 1):
        try:
            print("第%d次尝试。。。。" % i)
            driver = webdriver.Chrome()
            print("###########>>>>>>>开始打开上海交通网站<<<<<<<<<<#########")
            driver.get('http://www.sptcc.com/')
            print(driver.title)
            print("网站打开成功")
            sleep(2)
            print("查询公交卡号:%s" % cardID)
            driver.find_element_by_id("pL1i1").send_keys(cardID)
            driver.find_element_by_css_selector("a[class=\"pL1b1\"]").click()
            sleep(2)
            data = driver.find_element_by_css_selector("p[class=\"amt\"]").text
            print("公交卡 {0}  {1} ".format(cardID, data))
            driver.quit()
            return "公交卡 {0}  {1} \n".format(cardID, data)
            break
        except:
            print("查询出错。。。，再次尝试。。。")

    print("##################>>>>>>>退出查询<<<<<<<<<<##############")
    return "查询出错。。。"


if __name__ == '__main__':
    fromaddr = "*******@163.com"
    smtpaddr = "smtp.163.com"          # 163邮件smtp服务器地址
    toaddrs = ["*******@qq.com", "*******@163.com"]
    gj_info =''
    for cardID in cardIDList:
        gj_info += get_gj_info(cardID)
    subject = gj_info
    password = "*******"
    msg = gj_info
    sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)
```






