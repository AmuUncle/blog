---
title: QGraphicsView图形视图框架详解
date: 2023-05-13 11:00:12
categories: 
    - Qt进阶教程
tags: Qt
---

# QGraphicsView图形视图框架详解

## 什么是QGraphicsView？

QGraphicsView是Qt中的一个图形视图框架，它提供了一种方便的方式来显示和编辑大量的2D图形元素。QGraphicsView可以与QGraphicsScene一起使用，QGraphicsScene是一个2D图形场景，它包含了一组图形项，可以在其中添加、删除、移动和变换图形项。QGraphicsView提供了一种交互式的方式来显示和编辑QGraphicsScene中的图形项，包括平移、缩放、旋转、选择、拖拽等操作。

## QGraphicsView的基本用法

使用QGraphicsView需要以下几个步骤：

1. 创建一个QGraphicsScene对象，并在其中添加图形项。
2. 创建一个QGraphicsView对象，并将其设置为QGraphicsScene的视图。
3. 将QGraphicsView添加到窗口中，并显示出来。

下面是一个简单的示例代码，演示了如何使用QGraphicsView显示一个矩形和一个文本项：

```cpp
#include <QtWidgets>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QGraphicsScene scene;
    QGraphicsRectItem *rectItem = scene.addRect(QRectF(0, 0, 100, 100), QPen(Qt::black), QBrush(Qt::red));
    QGraphicsTextItem *textItem = scene.addText("Hello, QGraphicsView!");

    QGraphicsView view(&scene);
    view.show();

    return app.exec();
}
```

在上面的代码中，我们首先创建了一个QGraphicsScene对象，并在其中添加了一个矩形和一个文本项。然后，我们创建了一个QGraphicsView对象，并将其设置为QGraphicsScene的视图。最后，我们将QGraphicsView添加到窗口中，并显示出来。

## QGraphicsView的交互操作

QGraphicsView提供了一系列交互操作，可以方便地对QGraphicsScene中的图形项进行操作。下面是一些常用的交互操作：

- 平移：按住鼠标左键并拖动视图，可以平移视图。
- 缩放：使用鼠标滚轮可以缩放视图。
- 旋转：按住鼠标右键并拖动视图，可以旋转视图。
- 选择：单击图形项可以选择它，按住Ctrl键可以多选图形项。
- 拖拽：按住鼠标左键并拖动图形项，可以拖拽它。

下面是一个示例代码，演示了如何使用QGraphicsView的交互操作：

```cpp
#include <QtWidgets>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QGraphicsScene scene;
    QGraphicsRectItem *rectItem = scene.addRect(QRectF(0, 0, 100, 100), QPen(Qt::black), QBrush(Qt::red));
    QGraphicsTextItem *textItem = scene.addText("Hello, QGraphicsView!");

    QGraphicsView view(&scene);
    view.setRenderHint(QPainter::Antialiasing);
    view.setDragMode(QGraphicsView::ScrollHandDrag);
    view.setInteractive(true);
    view.show();

    return app.exec();
}
```

在上面的代码中，我们设置了QGraphicsView的渲染选项为抗锯齿，设置了拖拽模式为滚动手柄拖拽，并将交互模式设置为可交互。这样，我们就可以使用QGraphicsView的交互操作来操作QGraphicsScene中的图形项了。

## QGraphicsView的高级用法

除了基本用法和交互操作外，QGraphicsView还提供了一些高级用法，包括：

- 自定义视图：可以继承QGraphicsView类，并重写它的一些函数来实现自定义的视图。
- 自定义图形项：可以继承QGraphicsItem类，并重写它的一些函数来实现自定义的图形项。
- 图形项组合：可以将多个图形项组合成一个组，并对组进行操作。
- 图形项动画：可以使用QPropertyAnimation类来实现图形项的动画效果。

下面是一个示例代码，演示了如何使用QGraphicsView的高级用法：

```cpp
#include <QtWidgets>

class CustomView : public QGraphicsView
{
public:
    CustomView(QGraphicsScene *scene, QWidget *parent = nullptr) : QGraphicsView(scene, parent)
    {
        setRenderHint(QPainter::Antialiasing);
        setDragMode(QGraphicsView::ScrollHandDrag);
        setInteractive(true);
    }

protected:
    void wheelEvent(QWheelEvent *event) override
    {
        if (event->modifiers() & Qt::ControlModifier) {
            double scaleFactor = 1.15;
            if (event->delta() > 0) {
                scale(scaleFactor, scaleFactor);
            } else {
                scale(1 / scaleFactor, 1 / scaleFactor);
            }
            event->accept();
        } else {
            QGraphicsView::wheelEvent(event);
        }
    }
};

class CustomItem : public QGraphicsItem
{
public:
    CustomItem(QGraphicsItem *parent = nullptr) : QGraphicsItem(parent)
    {
        setFlag(QGraphicsItem::ItemIsMovable);
    }

    QRectF boundingRect() const override
    {
        return QRectF(-50, -50, 100, 100);
    }

    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget = nullptr) override
    {
        painter->setPen(Qt::black);
        painter->setBrush(Qt::yellow);
        painter->drawEllipse(-50, -50, 100, 100);
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QGraphicsScene scene;
    CustomItem *item = new CustomItem;
    scene.addItem(item);

    CustomView view(&scene);
    view.show();

    return app.exec();
}
```

在上面的代码中，我们首先创建了一个CustomView类，继承自QGraphicsView类，并重写了它的wheelEvent函数，实现了缩放视图的功能。然后，我们创建了一个CustomItem类，继承自QGraphicsItem类，并重写了它的boundingRect和paint函数，实现了一个自定义的图形项。最后，我们将CustomItem添加到QGraphicsScene中，并使用CustomView来显示QGraphicsScene。

通过上面的示例代码，我们可以看到QGraphicsView的高级用法非常灵活，可以根据需要进行自定义和扩展。如果您想要进一步了解QGraphicsView的高级用法，可以参考Qt官方文档或者相关书籍。
