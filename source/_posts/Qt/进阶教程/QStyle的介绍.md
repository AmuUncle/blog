---
title: QStyle的介绍
date: 2021-10-18 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

# QStyle的介绍

QStyle是Qt中一个用于自定义GUI外观的类，可以通过重写实现各种控件的显示效果。不同的Widget类有不同的默认样式，而通过QStyle，开发人员可以自定义整个应用程序，包括大小、颜色、字体和各种原始矢量图标。

## 基本用法

### 样式设置

通过调用QWidget或QApplication上的setStyle()函数选择特定的样式。

```cpp
QApplication a(argc, argv);
QStyle* myStyle = new MyCustomStyle();
a.setStyle(myStyle);
```

### 自定义样式

通过继承QStyle并实现其中的虚函数来实现GUI控件和窗口部件的自定义渲染样式。

以下是一个简单的样式子类定义示例：

```cpp
class CustomStyle : public QStyle
{
public:
    void drawPrimitive(PrimitiveElement element, const QStyleOption *option,
                        QPainter *painter, const QWidget *widget) const override;
};

void CustomStyle::drawPrimitive(PrimitiveElement element, const QStyleOption *option,
                                QPainter *painter, const QWidget *widget) const
{
    switch (element) {
        case PE_FrameFocusRect: {
            QPen pen(Qt::blue, 2, Qt::SolidLine, Qt::SquareCap, Qt::MiterJoin);
            painter->setPen(pen);
            painter->drawRect(option->rect.adjusted(0, 0, -1, -1));
            break;
        }
        default:
            QStyle::drawPrimitive(element, option, painter, widget);
            break;
    }
}
```

### 常用函数

QStyle提供了许多常见的方法以便对GUI控件进行设置和管理，例如：

* `polish()`：初始化QStyle对象（根据主题文件等优化样式）。
* `unpolish()`：撤销QStyle对象的初始化。
* `drawControl()`：为指定的GUI控件绘制样式。
* `styleHint()`：检索指定GUI样式的提示信息。
* `pixelMetric()`：检查特定的像素度量值。

例如，以下代码演示如何将原生风格的按钮改成红色背景：

```cpp
class RedButtonStyle : public QProxyStyle
{
public:
    QRect subElementRect(SubElement element, const QStyleOption *option, const QWidget *widget) const override
    {
        if (element == SE_PushButtonContents)
            return option->rect;
        else
            return QProxyStyle::subElementRect(element, option, widget);
    }

    void drawPrimitive(PrimitiveElement element, const QStyleOption *option, QPainter *painter, const QWidget *widget) const override
    {
        if (element == PE_PanelButtonCommand) {
            QBrush brush(QColor(Qt::red));
            painter->fillRect(option->rect, brush);
        }
        else {
            QProxyStyle::drawPrimitive(element, option, painter, widget);
        }
    }
};

QPushButton* redButton = new QPushButton("Red Button");
redButton->setStyle(new RedButtonStyle);
```

## 结论

总之，QStyle可以帮助Qt应用程序自定义外观风格并实现各种控件的渲染效果。QStyle允许开发人员自定义窗口部件和控件的样式以及大小、颜色、字体和矢量图标等属性。在实际应用中，需要根据具体的需求选择合适的方法继承并重写对应的函数，自定义Qt应用程序的外观和视觉效果。
