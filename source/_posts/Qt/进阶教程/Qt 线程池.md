---
title: Qt 线程池
date: 2021-11-22 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---


# Qt 线程池

Qt 线程池是 Qt 库中用于任务异步执行的工具类，它提供了一种简单方便的方式来管理多线程并发处理。本篇文章将会介绍 Qt 线程池的概念及其使用方法。

## 什么是线程池？

线程池是一个预先创建好一组线程，将可用线程保存在内存池中，等待来自任务队列的任务请求，一旦有任务到达就会自动分配空闲的线程来执行任务。线程执行完任务后并不会被立即销毁而是重新返回线程池中等待下次任务调度。

线程池在多线程编程中广泛应用，能够有效控制线程创建和线程销毁的频率，避免由于创建过多线程导致系统资源浪费和运行效率降低的问题。

## Qt 线程池的使用

### 引入头文件

为了使用 Qt 线程池，需要引入 `QtConcurrent/QtConcurrentRun` 头文件，实现如下：

```cpp
#include <QtConcurrent/QtConcurrentRun>
```

### 创建线程池

要使用 Qt 线程池，需要创建一个 `QThreadPool` 对象。 Qt 线程池默认使用线程数等于 CPU 核心数的两倍，但是你可以自定义线程数。创建线程池的代码如下：

```cpp
QThreadPool *threadPool = QThreadPool::globalInstance();
// or 
QThreadPool *threadPool = new QThreadPool(parent);
```

### 定义任务函数

需要执行在线程池中的任务必须是静态或全局的，这样才能保证在线程池中正确执行。为了方便演示，下面代码片段中使用 lambda 表达式作为任务函数：

```cpp
auto task = [](){
    QThread::sleep(1); // 模拟耗时操作
    qDebug() << "任务执行完毕";
};
```

### 提交任务

将任务提交到线程池中进行处理，使用 `QtConcurrent::run()` 函数即可。例如，以下代码可将 `task` 任务提交到线程池中：

```cpp
QtConcurrent::run(threadPool, task);
```

### 控制线程池

`QThreadPool` 对象有几个控制线程池行为的属性和方法：

- `setMaxThreadCount(int maxThreadCount)`：设置线程池最大线程数。
- `activeThreadCount()`：返回活跃线程个数。
- `reserveThread()`：分配一个新的线程，相当于增加一个已有线程的数量。
- `releaseThread()`：释放一个线程，相当于减少一个线程的数量。

### 等待任务完成

运行时，任务被提交到线程池中异步执行。想要等待所有的任务执行完成才继续后面的代码执行，可以使用 `QThreadPool::waitForDone()` 方法：

```cpp
threadPool->waitForDone();
```

## 总结

Qt 线程池提供了一种简单方便的方式来执行多线程并发操作，避免由于创建过多线程导致系统资源浪费和运行效率降低的问题。需要注意的是，在进行多线程并发处理时，必须保证代码的线程安全性。希望本文对 Qt 线程池的概念及使用方法有所帮助。
