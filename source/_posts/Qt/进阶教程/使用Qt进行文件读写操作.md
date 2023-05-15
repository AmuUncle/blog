---
title: 使用Qt进行文件读写操作
date: 2021-10-18 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

# 使用Qt进行文件读写操作

在现代应用程序中，处理文件读写操作是一项非常常见的任务。Qt提供了许多工具来轻松地读写文件。在本文中，我们将介绍如何使用Qt编写文件读写代码。

## QFile类

QFile是Qt中用于文件读写的核心类之一。要使用它进行读写操作，需要通过创建一个QFile对象来打开文件。例如，要打开一个名为example.txt的文本文件，并将其读入到一个QByteArray中，可以使用以下代码：

```cpp
#include <QFile>
#include <QDebug>

int main()
{
    const QString fileName = "example.txt";

    QFile file(fileName);

    if (!file.open(QIODevice::ReadOnly)) {
        qDebug() << "Failed to open file:" << fileName;
        return -1;
    }

    QByteArray content = file.readAll();

    qDebug() << "Content of file:" << fileName << ":" << endl << content;

    file.close();

    return 0;
}
```

要将数据写入文件，可以使用open函数来以写入模式打开文件，然后可以调用write函数，传入要包含在文件中的字节的指针和字节数：

```cpp
#include <QFile>
#include <QDebug>

int main()
{
    const QString fileName = "example.txt";

    QFile file(fileName);

    if (!file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        qDebug() << "Failed to open file:" << fileName;
        return -1;
    }

    QByteArray content = "Hello, world!";

    file.write(content);

    file.close();

    return 0;
}
```

## QTextStream类

QTextStream是Qt中用于文本文件读写的另一个核心类。它可以使用不同的编码，包括UTF-8、UTF-16等。例如，要将内容保存为UTF-8编码的文本文件，可以使用以下代码：

```cpp
#include <QFile>
#include <QTextStream>
#include <QDebug>

int main()
{
    const QString fileName = "example.txt";

    QFile file(fileName);

    if (!file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        qDebug() << "Failed to open file:" << fileName;
        return -1;
    }

    QTextStream out(&file);
    out.setCodec("UTF-8");

    out << "Hello, world!" << endl;

    file.close();

    return 0;
}
```

读取UTF-8编码的文本文件同样简单：

```cpp
#include <QFile>
#include <QTextStream>
#include <QDebug>

int main()
{
    const QString fileName = "example.txt";

    QFile file(fileName);

    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qDebug() << "Failed to open file:" << fileName;
        return -1;
    }

    QTextStream in(&file);
    in.setCodec("UTF-8");

    QString content = in.readAll();

    qDebug() << "Content of file:" << fileName << ":" << endl << content;

    file.close();

    return 0;
}
```

## 结论

在Qt中，文件读写操作非常简单。通过使用QFile和QTextStream类，可以轻松地读写各种类型的文件。
