---
title: QGraphicsDropShadowEffect的介绍
date: 2021-10-04 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

# QGraphicsDropShadowEffect的介绍

QGraphicsDropShadowEffect是Qt中一个用于添加阴影效果的图形特效类，可以在图形或控件周围添加一层阴影效果。通过调整阴影的偏移、模糊度、颜色等参数，可以实现各种独特的视觉效果。

## 基本用法

### 添加阴影

首先，在需要添加阴影效果的QWidget（或QGraphicsItem）对象上创建QGraphicsDropShadowEffect对象：

```cpp
QGraphicsDropShadowEffect *shadow = new QGraphicsDropShadowEffect(this);
```

然后，通过调整阴影效果的参数来实现不同的视觉效果。例如，以下代码将启用5个像素的模糊和45度向右下方的十六进制黑色阴影：

```cpp
shadow->setBlurRadius(5);
shadow->setOffset(3, 3);
shadow->setColor(QColor("#000000"));
```

将QGraphicsDropShadowEffect应用到相应的QWidget（或QGraphicsItem）对象上：

```cpp
myWidget->graphicsEffect() = shadow;
```

### 常用函数

QGraphicsDropShadowEffect提供了许多常见的方法以便对阴影进行设置和管理。例如：

* `setBlurRadius()`：设置阴影的模糊半径。
* `setOffset()`：设置阴影相对于原始控件的偏移量。
* `setColor()`：设置阴影颜色。
* `setOpacity()`：设置阴影透明度。
* `setEnabled()`：启用或禁用阴影效果。
* `boundingRectFor()`：计算产生的阴影下降Qt应用程序的范围。 

### 设置形状

如果需要将阴影限制在边框内，可以通过普通的设置形状来实现。

```cpp
QGraphicsDropShadowEffect *shadow = new QGraphicsDropShadowEffect(this);
QPainterPath path;
path.addRoundedRect(0, 0, width(), height(), 10, 10);
shadow->setBlurRadius(20);
shadow->setColor(QColor("#000000"));
shadow->setOffset(5,5);
setGraphicsEffect(shadow);
setMask(path.toFillPolygon().toPolygon());
```

上面代码表示一个圆角矩形的窗口，半径为10像素，向下偏移5个像素，以及黑色颜色和20像素半径的阴影。

## 结论

总之，QGraphicsDropShadowEffect提供了一种简单且灵活的方法来添加阴影效果以改善用户的视觉体验。开发人员可以通过更改阴影效果的参数来实现各种不同的视觉效果，通过对形状进行限制，来满足具体业务场景的需求。在实际应用中，根据需求选择适当的阴影效果参数，并注意不要过度使用阴影效果以免影响应用程序的性能。
