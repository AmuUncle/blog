---
title: QMetaObject::invokeMethod()的介绍
date: 2021-10-18 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

# QMetaObject::invokeMethod()的介绍

在Qt框架中，QMetaObject类提供了一些反射机制可以实现类似于Java反射机制的功能。其中一个函数就是QMetaObject::invokeMethod()，它可以通过字符串调用对象的方法，同时支持异步执行和跨线程操作等特性。

## 使用方法

QMetaObject::invokeMethod()方法有多个重载，最常用的格式如下：

```cpp
bool QMetaObject::invokeMethod(QObject *obj, const char *method,
        Qt::ConnectionType type = Qt::AutoConnection,
        QGenericReturnArgument ret = QGenericReturnArgument(),
        QGenericArgument val0 = QGenericArgument(),
        QGenericArgument val1 = QGenericArgument(),
        QGenericArgument val2 = QGenericArgument(),
        QGenericArgument val3 = QGenericArgument(),
        QGenericArgument val4 = QGenericArgument(),
        QGenericArgument val5 = QGenericArgument(),
        QGenericArgument val6 = QGenericArgument(),
        QGenericArgument val7 = QGenericArgument(),
        QGenericArgument val8 = QGenericArgument(),
        QGenericArgument val9 = QGenericArgument());
```

* `obj`：要调用方法的QObject对象指针。
* `method`：需要调用的方法名字符串。
* `type`：连接类型，决定调用方法的线程以及调用形式。其值可以是Qt::DirectConnection（同步直接调用）、Qt::QueuedConnection（异步排队调用）和Qt::AutoConnection（根据线程自动选择同步直接调用或异步排队调用）。
* `ret`：返回值类型。可以使用QGenericReturnArgument分别传入不同的返回类型，通常为void。
* `val0～val9`：可选的十个参数值，根据需要传递。

## 使用示例

下面是一个使用QMetaObject::invokeMethod()来调用另一个对象函数的例子：

```cpp
#include <QThread>
#include <QDebug>

class MyWorker : public QObject
{
    Q_OBJECT

public:
    explicit MyWorker(QObject *parent = nullptr) : QObject(parent) {}

signals:
    void finished();
    void progressMade(int value);

public slots:
    void doWork()
    {
        for (int i = 0; i <= 100; ++i) {
            emit progressMade(i);
            QThread::msleep(50);
        }
        emit finished();
    }
};

class MyObject : public QObject
{
    Q_OBJECT

public:
    explicit MyObject(QObject *parent = nullptr) : QObject(parent) {}

public slots:
    void onWorkerFinished()
    {
        qDebug() << "Worker finished.";
    }

    void onWorkerProgressMade(int value)
    {
        qDebug() << "Progress made:" << value;
    }
};

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    MyWorker worker;
    MyObject obj;

    QObject::connect(&worker, &MyWorker::finished,
                     &a, &QCoreApplication::quit);
    QObject::connect(&worker, &MyWorker::progressMade,
                     &obj, "onWorkerProgressMade");

    QMetaObject::invokeMethod(&worker, "doWork");

    return a.exec();
}
```

在这个例子中，我们定义了一个MyWorker类和一个MyObject类。其中MyWorker类是一个计时器类，通过发射信号告诉外部工作进度情况。另一方面，MyObject类提供了两个槽函数onWorkerFinished()和onWorkerProgressMade()，用于处理MyWorker类的信号。

在main函数中，我们首先创建了worker和obj对象，然后使用`&worker, "doWork"`这种方式（即字符串调用）来调用MyWorker类中的doWork()方法，实现异步操作并执行worker对象的计时器操作。

## 注意事项

* 方法名字符串必须与槽函数名或者信号名字匹配。
* 只有公共槽函数才能使用该方法调用，无法调用私有、保护槽函数及任何静态函数。
* 参数根据调用的函数需要自行配置，使用过程中需要注意参数顺序和数据类型。
* 调用时需要保证目标对象已经完成构造，并且处于合法状态。

## 结论

总之，QMetaObject::invokeMethod()函数是一个非常方便的反射调用方法，可以让我们避免在跨线程信号连接中频繁考虑线程安全问题，简化代码流程，带来更好的编程体验。
