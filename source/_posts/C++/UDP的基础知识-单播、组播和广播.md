---
title: UDP的基础知识-单播、组播和广播
date: 2023-5-12 13:52:41
categories: C++基础
tags: 
    - C++
    - 网络通信
---

## UDP的基础知识

UDP（User Datagram Protocol）是一种无连接协议，它将数据报文发送出去，由接收端来进行处理。UDP不提供可靠性，也不保证数据的正确性和顺序。但是，UDP具有较低的延迟和较少的开销。在网络游戏、视频流传输、DNS等应用中广泛使用。

UDP使用IP协议来传输数据，每个UDP数据包被封装在一个IP数据包中并通过网络的其他节点进行路由。UDP使用端口来标识不同应用程序之间的通信，并为每个UDP数据包提供源端口和目的端口。源端口和目标端口的结合形成了一个套接字（socket），套接字可以唯一标识两个应用程序之间的单独的会话。

## 单播

**单播（Unicast）** 是一对一通信模式，在这种模式下，一个发送者向一个接收者发送数据包。单播通过以下程序示例实现：

```c++
#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <cstring>

using namespace std;

int main() {
    // 创建一个IPv4 UDP套接字
    int sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    // 构造服务器地址
    struct sockaddr_in server_addr;
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8888);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // 发送数据
    char buf[] = "Hello, this is a unicast message!";
    sendto(sockfd, buf, strlen(buf), 0, (struct sockaddr *)&server_addr, sizeof(server_addr));

    // 关闭套接字
    close(sockfd);

    return 0;
}
```

在上面的程序中，我们使用`socket`函数创建了一个IPv4 UDP套接字，并使用`sendto`函数向指定的服务器IP地址和端口发送数据包。

## 组播

组播是一种用于在网络中向多个接收方同时传输数据的通信方式。在UDP协议中，组播使用特定的IP地址范围（224.0.0.0 - 239.255.255.255）进行标识。发送方通过将数据包发送到组播地址，而不是单独的目标地址，可以将数据传输给一组接收方。

组播需要使用专门的协议支持，如IGMP（Internet Group Management Protocol），以便确定哪些接收方对该组播感兴趣，并将数据包路由到正确的接收方。

在C++中使用UDP进行组播的示例代码如下：

```c++
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

#define PORT 8888
#define GROUP "239.0.0.1"

int main()
{
    struct sockaddr_in addr;
    int sock, cnt;
    char message[] = "Hello, multicast!";
    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if(sock < 0)
    {
        perror("socket");
        exit(EXIT_FAILURE);
    }
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(GROUP);
    addr.sin_port = htons(PORT);
    while(1)
    {
        cnt = sendto(sock, message, sizeof(message), 0, (struct sockaddr *)&addr, sizeof(addr));
        if(cnt < 0)
        {
            perror("sendto");
            exit(EXIT_FAILURE);
        }
        sleep(1);
    }
    close(sock);
    return 0;
}
```

在上述代码中，使用`socket()`函数创建一个UDP套接字并指定组播的IP地址和端口号。发送方通过`sendto()`函数将数据包发送到组播地址，并以一定的时间间隔重复执行此操作。

## 广播

广播是另一种用于向一组接收方传输数据的通信方式，在网络中向同一子网中的所有主机发送数据包。在IPv4网络中，广播使用特殊的IP地址（255.255.255.255）进行标识。

在C++中使用UDP进行广播的示例代码如下：

```c++
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

#define PORT 8888
#define BROADCAST "255.255.255.255"

int main()
{
    struct sockaddr_in addr;
    int sock, cnt;
    char message[] = "Hello, broadcast!";
    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if(sock < 0)
    {
        perror("socket");
        exit(EXIT_FAILURE);
    }
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(BROADCAST);
    addr.sin_port = htons(PORT);
    int optval = 1;
    setsockopt(sock, SOL_SOCKET, SO_BROADCAST, &optval, sizeof(optval));
    while(1)
    {
        cnt = sendto(sock, message, sizeof(message), 0, (struct sockaddr *)&addr, sizeof(addr));
        if(cnt < 0)
        {
            perror("sendto");
            exit(EXIT_FAILURE);
        }
        sleep(1);
    }
    close(sock);
    return 0;
}
```

在上述代码中，使用`socket()`函数创建一个UDP套接字并指定广播的IP地址和端口号。发送方通过`setsockopt()`函数将`SO_BROADCAST`选项设置为启用广播功能，并使用`sendto()`函数将数据包发送到广播地址，并以一定的时间间隔重复执行此操作。


### 总结

单播、组播和广播都是UDP协议中常用的通信方式。单播适用于点对点的通信，组播和广播适用于向多个接收方传输数据。其中组播需要使用IGMP协议支持，并使用特定的IP地址范围进行标识；广播需要使用特殊的IP地址（255.255.255.255）进行标识，并启用`SO_BROADCAST`选项。

在C++中，可以使用`socket()`函数创建UDP套接字，并使用`sendto()`函数将数据包发送到目标地址、组播地址或广播地址，以实现单播、组播和广播功能。

