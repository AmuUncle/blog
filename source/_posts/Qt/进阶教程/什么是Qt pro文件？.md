---
title: 什么是Qt pro文件？
date: 2021-10-22 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

## 什么是Qt pro文件？

Qt pro文件是QT项目管理器使用的配置文件。它们在Qt创建时自动生成，并且包含有关工程的信息，如源文件、库和编译选项等。

## 如何创建Qt pro文件？

可以使用Qt Creator创建交互式工程向导来创建一个新项目并自动生成pro文件。也可以手动创建pro文件并将其添加到Qt Creator项目中。 

## pro文件的基本语法结构

```qmake
CONFIG += <配置选项>
TARGET = <目标名>
TEMPLATE = <模板>

<其他变量>

SOURCES += <源文件列表>
HEADERS += <头文件列表>
FORMS += <表单文件列表>
RESOURCES += <资源文件列表>
LIBS += <链接库列表>
```

其中，`CONFIG` 指定一系列的配置选项，例如设置编译类型：`debug` 或 `release`；`TEMPLATE` 指定使用什么样的构建模板，例如 `app` 或 `lib`； `TARGET` 是生成的最终目标（可执行文件，静态/共享库）的名称；`SOURCES`、`HEADERS`、`FORMS` 和`RESOURCES` 分别指定源文件、头文件、表单和资源文件的列表；`LIBS` 定义所需的库文件。 

## Qt pro文件示例

```qmake
# 配置debug/release下的编译选项 
CONFIG += debug_and_release

# 指定生成的目标为可执行文件
TEMPLATE = app

# 定义可执行文件名 
TARGET = myapp

# 声明源文件目录 
SOURCES += main.cpp \
           mywindow.cpp

# 声明头文件目录
HEADERS += mywindow.h 

# 配置Qt库（示例中使用了 Widgets） 
QT += widgets

# 添加外部库 
LIBS += -lmylib
```

以上示例将生成一个名为 `myapp` 的可执行文件，包含 `main.cpp` 和 `mywindow.cpp` 文件。其中所需的头文件 `mywindow.h` 将被包含在编译中。该应用程序将链接到名为 `mylib` 的外部库，并且它将使用 Qt 库中的一个库（widgets）。 

这是一个简单的Qt pro文件的例子，开发者可以根据需要和实际情况进行修改和扩展。