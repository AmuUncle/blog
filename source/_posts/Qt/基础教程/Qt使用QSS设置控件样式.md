
---
title: Qt使用QSS设置控件样式
date: 2021-10-02 10:34:06
categories: Qt基础教程
tags: Qt
---

# Qt使用QSS设置控件样式

在这篇文章中，我们将会学习如何使用QSS（Qt样式表）来自定义QPushButton、QLabel、QLineEdit和QComboBox控件的样式。在Qt中，我们可以使用QSS来定制控件的外观，并且能够方便地整合到我们的应用程序中。

## 设置QPushButton的样式

我们可以通过以下方式设置QPushButton的样式：

```cpp
QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #3b78e6, stop:1 #0f5fd7);
    border-radius: 5px;
    color: white;
    font-weight: bold;
    padding: 5px 15px;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #60a3f7, stop:1 #3b78e6);
}

QPushButton:pressed {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0f5fd7, stop:1 #3b78e6);
}
```

在这里，我们将QPushButton控件的背景设置为颜色渐变，使用了border-radius属性添加圆角边框。我们还改变了字体加粗程度和颜色，并且为按钮设置了padding属性。同时，我们还在:hover和:pressed状态下分别修改按钮的渐变背景色。

## 设置QLabel的样式

与QPushButton的设置方式相似，我们可以使用以下代码来设置QLabel的样式：

```cpp
QLabel {
    background-color: #d8e5f4;
    border: 1px solid #c7d9ea;
    color: #333333;
    padding: 2px;
}
```

对于QLabel控件，我们将其背景设置为固定的颜色，在边界中添加了细的灰色边框，并为文本设置了适当的内边距。

## 设置QLineEdit的样式

我们可以使用以下代码来设置QLineEdit的样式：

```cpp
QLineEdit {
    background-color: #ffffff;
    border: 1px solid #c7d9ea;
    color: #444444;
    padding: 2px;
}

QLineEdit:focus {
    border: 1px solid #3b79e6;
    outline: none;
}
```

这里，我们设置了QLineEdit控件的背景色和边框颜色，使其看起来更加干净。对于焦点情况，我们添加了一个以蓝色突出表示的边框线，并禁用了默认的外观字体样式应用。

## 设置QComboBox的样式

最后，我们使用以下代码来设置QComboBox的样式：

```cpp
QComboBox {
    background-color: #ffffff;
    border: 1px solid #c7d9ea;
    color: #444444;
    padding: 2px;    
}

QComboBox:editable {
    background-color: #ffffff;
}

QComboBox QAbstractItemView {
    border: 1px solid #c7d9ea;
    selection-background-color: #3b78e6;
    selection-color: white;
}
```

在这里，我们设置了QComboBox控件的背景色和边框颜色，以及它的文本颜色并添加了适当的内边距。对于可编辑的QComboBox，我们还单独为其设置了背景色。最后，我们修改QComboBox中项目视图的边框线，并为选中的项提供了更明显的文本和渐变背景颜色。

在本篇文章中，我们学习了如何使用QSS来自定义QPushButton、QLabel、QLineEdit和QComboBox控件的外观样式。Qt提供了很多的属性可以帮助我们改变控件的外观，并且使得我们可以创建具有自定义外观的应用程序。