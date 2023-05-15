---
title: QFont中setPointSize和setPixelSize的作用和区别
date: 2021-10-05 16:34:06
categories: Qt基础教程
tags: Qt
---

# QFont中setPointSize和setPixelSize的作用和区别

在Qt应用程序中，字体往往是UI设计中非常重要的一个因素。QFont类是Qt框架中表示字体的核心类，它提供了许多方法来指定字体外观和大小等属性。其中，setPointSize()和setPixelSize()是QFont中我们最常见也非常实用的两个方法之一，本文将给出它们的作用和区别。

## setPointSize()

setPointSize()方法是QFont类的方法之一，它可以设置字体的点数大小。字号通常参数是数字(N)，其默认值为（11）。

当我们调用setPointSize()方法时，QFont将点数大小与每英寸点数分辨率结合计算出每个字符的高度。 在这种情况下，如果QFontMetrics返回像素数，则会将该字段转换为点数大小。

示例代码如下：

```cpp
QFont font("Times", 11);
font.setPointSize(14);       // 将字体点数大小设置为 14
```

在上述示例中，我们创建了一个名为“font”的新字体对象，并使用它的setPointSize()方法将点数大小设置为14。这就意味着此字体的所有字符都将具有14个点的高度。

## setPixelSize()

setPixelSize()方法是QFont类的另一个方法，它可以设置字体的像素大小。

当使用setPixelSize()方法时，字体的大小将以像素为单位而不是点数来测量。注意：大小实际上仍然被视为点值——QFontMetrics基于其当前分辨率将其转换为像素。

示例代码如下：

```cpp
QFont font("Times", 11);
font.setPixelSize(18);       // 将字体像素大小设置为 18
```

在上述示例中，我们创建了一个名为“font”的新字体对象，并使用它的setPixelSize()方法将像素大小设置为18。这意味着，在至少可能的QFontMetrics（即与屏幕分辨率相同的值），此字体对象的每个字符将具有18个像素高度。

## 区别

我们可以看到，setPointSize()和setPixelSize()都提供了一种设置字体大小的方法。主要区别在于它们使用的单位不同：setPointSize()方法使用点数作为单位，而setPixelSize()方法使用像素作为单位。因此，不同分辨率下的字体实际显示效果也会有所不同。

通常情况下，为了更好的UI效果，建议优先考虑使用setPixelSize()方法来设置字体大小，以确保字体在不同设备上显示效果的一致性。但是需要注意的是，使用像素单位设置字体大小可能导致文字在高分辨率设备上显示得过小或过大，因此我们需要根据具体需求进行选择。

## 结论

在Qt应用程序中，字体往往是UI设计中非常重要的一个因素。setPointSize()和setPixelSize()方法是QFont类中最基本、实用的设置字体大小的方法之一。它们的区别在于使用的单位和实际显示效果会有所不同，因此在选择时需要结合具体需求进行选择。
