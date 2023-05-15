---
title: Qt创建一个动画按钮
date: 2021-09-28 16:34:06
categories: Qt基础教程
tags: Qt
---

# Qt创建一个动画按钮

在这篇博客中，我们将会学习如何通过使用Qt来创建一个动画按钮。我们将会使用QPropertyAnimation类，它可以使我们控制一个对象的任何属性的动画。

## 第1步 - 创建按钮

首先，我们需要创建一个QPushButton对象来表示我们的动画按钮。我们可以使用以下代码：

```cpp
QPushButton *button = new QPushButton("Click me", parent);
```

这将会创建一个带有“Click me”文本的QPushButton对象，并且将其添加到指定的父QWidget对象中。

## 第2步 - 为按钮设置动画属性

接下来，我们需要为按钮设置属性，以便我们可以通过动画来改变它们。在这个例子中，我们将会为按钮的大小和颜色属性设置动画。我们可以使用以下代码：

```cpp
QPropertyAnimation *animation = new QPropertyAnimation(button, "geometry");
animation->setDuration(1000);
animation->setStartValue(QRect(0, 0, 100, 30));
animation->setEndValue(QRect(250, 250, 200, 60));
animation->setEasingCurve(QEasingCurve::InOutQuad);
animation->start();
```

这里我们创建一个QPropertyAnimation对象，然后将其连接到按钮上，并将其属性设置为几何形状。我们还将动画时长设置为1000毫秒，起始和终止值设置为按钮的初始和最终位置（这里的值是矩形区域，我们可以设置其大小和位置），并且动画曲线设置为QEasingCurve::InOutQuad，以使动画具有平滑的效果。最后我们调用start()函数开始动画。

## 第3步 - 运行程序

现在我们可以运行程序，并点击按钮观看它的动画效果啦！完整的Qt程序代码应该如下所示：

```cpp
#include <QPushButton>
#include <QPropertyAnimation>
#include <QEasingCurve>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QWidget *parent = new QWidget;
    parent->setFixedSize(500, 500);

    QPushButton *button = new QPushButton("Click me", parent);
    button->setGeometry(0, 0, 100, 30);

    QPropertyAnimation *animation = new QPropertyAnimation(button, "geometry");
    animation->setDuration(1000);
    animation->setStartValue(QRect(0, 0, 100, 30));
    animation->setEndValue(QRect(250, 250, 200, 60));
    animation->setEasingCurve(QEasingCurve::InOutQuad);
    animation->start();

    parent->show();
    return app.exec();
}
```

恭喜你，你已经学会了如何通过Qt创建一个动画按钮！