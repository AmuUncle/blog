---
title: Qt高级绘图
date: 2021-10-03 10:34:06
categories: Qt基础教程
tags: Qt
---

# Qt高级绘图

在这篇文章中，我们将会介绍Qt中的高级绘制技术，并了解如何使用它们来实现自定义的绘制和渲染。Qt提供了一些专业级别的API来进行绘图操作，可以创建矢量图形或者像素颜色（bitmap）图形。

## QPainter绘图框架

Qt中最常用的绘制API是QPainter类。它可以用于将几何形状、图像和文本等内容绘制到窗口或Widge上。

以下是一个简单的例子，展示如何使用QPainter在QWidget上绘制一条直线：

```cpp
void CustomWidget::paintEvent(QPaintEvent* event) {
    QPainter painter(this);
    painter.drawLine(0, 0, width(), height());
}
```
首先，我们重载QWidget的paintEvent()函数，在其参数event中派生一个QPainter对象，然后使用drawLine()函数在CustomWidget委托的窗口上绘制一条直线。

## 手动绘画：绘制基本图元

通过手动绘制，我们可以创建自定义的图形界面，通常需要使用以下的基本图形元素：线条、多边形、椭圆、弧形和文字等。

例如，下面是一个绘制圆形和矩形的例子：

```cpp
void CustomWidget::paintEvent(QPaintEvent* event) {
    QPainter painter(this);
    painter.setBrush(QBrush(Qt::black));
    painter.drawEllipse(QRectF(20, 20, 50, 50));
    painter.drawRect(QRectF(80, 20, 50, 50));
}
```
在这个例子中，我们重载QWidget的paintEvent()函数，并使用QPainter类在CustomWidget委托的窗口上绘制了一个圆和矩形。注意：由于Qt计算尺寸是采用浮点类型的矩形标准，我们使用QRectF来定义矩形。

## 高级绘图：OpenGL

除了Qt自带的绘图API，Qt还支持OpenGL，通常可用于高性能、多次运动的环境中，如游戏或数据科学等。

例如，以下代码展示了如何在QWidget上绘制三角形（当OpenGL开启时）：

```cpp
void CustomWidget::paintEvent(QPaintEvent* event) {
#ifdef QT_OPENGL_SUPPORT
    QOpenGLWidget* widget = new QOpenGLWidget(this);
    widget ->makeCurrent();
    glBegin(GL_TRIANGLES);
    glVertex2f(-1.0f,-0.5f);
    glVertex2f( 1.0f,-0.5f);
    glVertex2f( 0.0f, 0.5f);
    glEnd();
    glFlush();  
#else
    QPainter painter(this);
    // 使用QPainter API 绘制其他内容
#endif
}
```

在这个例子中，我们创建了一个QOpenGLWidget对象，并调用它的makeCurrent()方法获取OpenGL渲染环境。

接着，我们使用OpenGL API绘制三角形，并调用glFlush()函数刷新缓冲区来呈现图像。

在不支持OpenGL的情况下（如运行在低端硬件或嵌入式设备上），我们可以使用QPainter API替代OpenGL的功能，或者提供本地CPU的软件渲染方式。

## 总结

Qt提供了多种高级绘制技术，可以帮助我们实现精美的UI界面和高性能的数据可视化。通过手动绘图和OpenGL，我们可以创造出令人惊叹的艺术作品和复杂的3D场景展示。
