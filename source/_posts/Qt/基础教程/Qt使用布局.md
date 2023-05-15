---
title: Qt使用布局
date: 2021-10-03 10:34:06
categories: Qt基础教程
tags: Qt
---

# Qt使用布局

在这篇文章中，我们将会介绍Qt中的各种布局方式，以及如何使用它们来管理控件的位置和大小。在Qt中有很多种布局，我们可以根据不同的需求选择不同的布局方式。

## 布局管理器

在Qt中，布局管理器是用来自动调整窗口中包含控件的位置和大小的。Qt提供了四种常用的布局管理器：QHBoxLayout、QVBoxLayout、QGridLayout和QFormLayout。它们的主要不同在于它们如何管理和排列窗口中的控件。

## QHBoxLayout布局

QHBoxLayout，也称为水平布局，适用于在一个水平行上对控件进行排列。以下代码将帮助你创建并实现QHBoxLayout布局：

```cpp
QHBoxLayout* layout = new QHBoxLayout;
layout ->addWidget(w1);
layout ->addWidget(w2);
...
setLayout(layout);
```

这里我们首先创建了一个QHBoxLayout对象，接着将控件w1、w2等添加到内部，然后将该布局设置给当前的容器QWidget，例如MainWindow或其他定制化的窗口。当我们使用setGeometry()或resize()函数调整主窗口大小时，布局管理器将自动调整子控件的位置和大小。

## QVBoxLayout布局

相对于QHBoxLayout水平布局， QVBoxLayout是垂直布局，适用于在一个垂直列上对控件进行排列。下面演示如何创建并实现QVBoxLayout：

```cpp
QVBoxLayout* layout = new QVBoxLayout;
layout ->addWidget(w1);
layout ->addWidget(w2);
...
setLayout(layout);
```

与QHBoxLayout相似，我们创建一个QVBoxLayout对象，并将控件添加到内部，然后将该布局设置给当前的窗口或窗体。

## QGridLayout布局

QGridLayout是将控件放置在二维网格中布局的一种方式。以下代码将帮助你创建并实现QGridLayout布局：

```cpp
QGridLayout* layout= new QGridLayout;
layout->addWidget(w1,0,0);     //这里 0 表示行 0 ， 0 表示列 0 
layout->addWidget(w2,0,1);
layout->addWidget(w3,1,0,1,2); //这里 1 表示行 1 ， 0 表示列 0， 1 行 2 列
setLayout(layout);
```

在这里，我们首先创建一个QGridLayout对象，并使用addWidget()函数将控件w1、w2等添加到内部，使用（x,y）、rowSpan和colSpan参数指定需要占据的单元格信息，例如：3行2列布局，w3 占据其中2列，起始点为第2行第0列（注意：坐标从0开始）。

## QFormLayout布局

QFormLayout旨在用于简单的表单布局，特别是标签/输入组合。以下代码将帮助你创建并实现QFormLayout布局：

```cpp
QFormLayout* layout= new QFormLayout;
layout->addRow("标签 1", w1);
layout->addRow("标签 2", w2);
...
setLayout(layout);
```

在这里，我们使用addRow()函数将控件w1、w2等添加到内部，并添加相应的标签。

## 总结

在Qt中有很多种布局方式，我们应该选择适用于特定需求的布局方式。当然，这里只是介绍了几种主要的布局管理器，Qt还有其他布局可供选择，例如：QStackedlayout、QSplitter等；在使用时需要按照实际场景进行选择。布局管理器的作用是自动调整和管理控件位置和大小，并确保它们能够自动适应不同分辨率和窗口尺寸的变化，从而使得GUI编程更加方便简单。