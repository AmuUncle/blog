---
title: 使用Qt实现HTTP中GET、POST、PUT、DELETE
date: 2021-10-18 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

# 使用Qt实现HTTP中GET、POST、PUT、DELETE

在现代的应用程序中，网络连接已成为不可或缺的一部分。这就意味着您必须编写代码来执行各种请求和响应操作。本文将向您展示如何使用Qt库来实现HTTP中GET、POST、PUT、DELETE等基本请求，并解释每个请求行动背后的重要细节和选项。

## 前置条件

首先，确保您的项目已正确链接Qt网络模块并包含它所需的头文件：

```cpp
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
```

## GET请求

GET请求是最常见的HTTP请求类型之一。此请求类型从服务器请求指定的资源，没有请求正文，仅有URL和请求头。

以下是一个简单的使用Qt的GET请求的示例：

```cpp
void performGetRequest(QUrl url)
{
    QNetworkAccessManager manager;
    QNetworkRequest request(url);

    QNetworkReply* reply = manager.get(request);
    connect(reply, &QNetworkReply::finished, [reply](){
        if (reply->error() != QNetworkReply::NoError) {
            qDebug() << "Error in performing get request: " << reply->errorString();
            reply->deleteLater();
            return;
        }
        QByteArray data = reply->readAll();
        qDebug() << "Received data: " << data;
        reply->deleteLater();
    });
}
```

我们首先创建一个QNetworkAccessManager对象，然后创建一个QNetworkRequest，然后使用get()函数执行GET请求。我们使用finished()信号和一个lambda表达式来读取响应数据并清理资源。

## POST请求

POST请求是向Web服务器提交信息的常见方法。与GET请求不同，POST包含请求正文，并且通常用于将表单数据提交到服务器。下面是一个简单使用Qt中POST请求的示例：

```cpp
void performPostRequest(QUrl url, QVariantMap data)
{
    QNetworkAccessManager manager;
    QNetworkRequest request(url);
    request.setHeader(QNetworkRequest::ContentTypeHeader, "application/x-www-form-urlencoded");

    QByteArray postData;
    for (auto key : data.keys()) {
        postData.append(key.toLatin1()).append("=").append(data[key].toByteArray()).append("&");
    }
    if (postData.endsWith("&")) {
        postData.chop(1);
    }

    QNetworkReply* reply = manager.post(request, postData);
    connect(reply, &QNetworkReply::finished, [reply](){
        if (reply->error() != QNetworkReply::NoError) {
            qDebug() << "Error in performing post request: " << reply->errorString();
            reply->deleteLater();
            return;
        }
        QByteArray data = reply->readAll();
        qDebug() << "Received data: " << data;
        reply->deleteLater();
    });
}
```

在这里，我们创建了一个QNetworkRequest并为其设置一些HTTP标头，然后将数据映射到post请求正文中，最后使用post()函数执行POST请求。同样，使用finished()信号和一个lambda表达式来处理响应数据。

## PUT请求

PUT请求主要用于更新服务器上的资源，可以用于创建新资源。与POST类似，PUT请求包含一个请求正文。下面是如何在Qt中执行PUT请求的示例：

```cpp
void performPutRequest(QUrl url, QByteArray data)
{
    QNetworkAccessManager manager;
    QNetworkRequest request(url);

    QBuffer *buffer = new QBuffer;
    buffer->setData(data);
    request.setHeader(QNetworkRequest::ContentTypeHeader, "application/octet-stream");

    QNetworkReply* reply = manager.put(request, buffer);
    connect(reply, &QNetworkReply::finished, [reply, buffer](){
        if (reply->error() != QNetworkReply::NoError) {
            qDebug() << "Error in performing put request: " << reply->errorString();
            reply->deleteLater();
            buffer->deleteLater();
            return;
        }
        QByteArray responseData = reply->readAll();
        qDebug() << "Received data: " << responseData;
        reply->deleteLater();
        buffer->deleteLater();
    });
}
```

在这里，我们创建了一个指向QBuffer对象的指针，它用于传递数据主体和管理内存。可选地，我们可以设置一些HTTP标头。

## DELETE请求

DELETE请求用于删除服务器上的资源，通常用于删除文件或恢复从数据库删除的条目。以下是如何使用Qt执行DELETE请求的示例：

```cpp
void performDeleteRequest(QUrl url)
{
    QNetworkAccessManager manager;
    QNetworkRequest request(url);

    QNetworkReply* reply = manager.deleteResource(request);
    connect(reply, &QNetworkReply::finished, [reply](){
        if (reply->error() != QNetworkReply::NoError) {
            qDebug() << "Error in performing delete request: " << reply->errorString();
            reply->deleteLater();
            return;
        }
        QByteArray responseData = reply->readAll();
        qDebug() << "Deleted data: " << responseData;
        reply->deleteLater();
    }
}
```

我们首先创建一个QNetworkAccessManager对象，然后创建一个QNetworkRequest，然后使用deleteResource()函数执行GET请求。我们使用finished()信号和一个lambda表达式来读取响应数据并清理资源。
