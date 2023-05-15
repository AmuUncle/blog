---
title: Qt中使用TCP服务端及客户端
date: 2021-10-05 16:34:06
categories: Qt基础教程
tags: Qt
---

# Qt中使用TCP服务端及客户端

TCP（Transmission Control Protocol）是一种可靠、高度优化的互联网通信协议，广泛用于各类网络应用程序中。在这篇博客中，我们将介绍如何在Qt中使用TCP服务端及客户端。

## 使用Qt创建TCP服务器

要使用Qt创建TCP服务器，需要完成以下步骤：

### 步骤1：创建QTcpServer对象

```cpp
QTcpServer *server = new QTcpServer(this);
```

### 步骤2：监听连接请求

在开始监听之前，您需要使用listen()方法指定服务端口号并监听来自特定IP地址的连接请求。

```cpp
if (!server->listen(QHostAddress::Any, 12345))
{
    qDebug() << "Failed to start server";
    return;
}
```

### 步骤3：处理新连接请求

每当一个新连接请求到达服务器时，QTcpServer将通过发射newConnection()信号来提示您。您可以使用accept()方法来接受该连接，并创建一个新的QTcpSocket对象以进行收发消息。

```cpp
void MyTcpServer::newConnection()
{
    QTcpSocket *socket = server->nextPendingConnection();
    connect(socket, SIGNAL(readyRead()), this, SLOT(readData()));
    connect(socket, SIGNAL(disconnected()), socket, SLOT(deleteLater()));
}

void MyTcpServer::readData()
{
    QTcpSocket *socket = static_cast<QTcpSocket *>(sender());
    QByteArray data = socket->readAll();
    // 处理接收到的数据
}
```

### 步骤4：发送数据

使用QTcpSocket的write()方法将您的数据发送到连接的客户端。

```cpp
socket->write("Hello world");
```

## 使用Qt创建TCP客户端

要使用Qt创建TCP客户端，需要完成以下步骤：

### 步骤1：创建QTcpSocket对象

```cpp
QTcpSocket *m_socket = new QTcpSocket(this);
```

### 步骤2：连接到服务器

使用connectToHost()方法将socket连接到目标主机和端口。连接成功后，QTcpSocket将发送connected()信号。

```cpp
m_socket->connectToHost(QHostAddress("127.0.0.1"), 12345);
```

### 步骤3：发送和接收数据

使用write()方法向服务器发送数据，并通过readyRead()信号处理接收到的数据。

```cpp
void MyTcpClient::sendData(QString data)
{
    m_socket->write(data.toUtf8().constData());
}

void MyTcpClient::readData()
{
    QString data = m_socket->readAll();
    // 处理接收到的数据
}
```

## 总结

在Qt中使用TCP服务端及客户端是一种可靠、高效的方法来进行网络通信。QTcpServer和QTcpSocket类提供了一个面向对象的解决方案，使得您能够轻松地开发出各种类型的网络应用程序。

然而，请注意因多种原因（例如网络中断、远程主机关闭连接等）导致的时延和异常情况，并确保在代码中处理这些情况以确保应用程序的稳定性。
