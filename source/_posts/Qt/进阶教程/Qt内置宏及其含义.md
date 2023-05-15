---
title: Qt内置宏及其含义
date: 2021-11-22 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

# Qt内置宏及其含义

当您开始使用Qt编程时，会发现在Qt代码中频繁出现了各种奇怪的宏定义。它们是用于执行不同功能的特殊指令。在Qt中有许多这样的宏定义。在本篇教程中，我们将深入探讨这些宏的含义和用法。

## Q_OBJECT

`Q_OBJECT` 是一个非常重要的宏。它必须出现在 Qt 类声明的私有部分中。该宏告诉 Qt 元对象编译器在 MOC (Meta-Object Compiler) 中为该类生成元对象。这使得信号和槽、元数据等特性得以使用。例如：

```c++
class MyWidget : public QWidget
{
    Q_OBJECT

public:
    explicit MyWidget(QWidget *parent = nullptr);

signals:
    void buttonClicked();

private slots:
    void handleButton();
};
```

注意：如果您使用的 IDE 不支持自动运行 MOC，您需要确保在每次更改包含 `Q_OBJECT` 的头文件之后手动运行 MOC。

## Q_PROPERTY

`Q_PROPERTY` 宏用于声明属性。它与访问器方法一起使用，以便更方便地查询和设置属性值。例如：

```c++
class MyWidget : public QWidget
{
    Q_OBJECT
    Q_PROPERTY(QString text READ text WRITE setText NOTIFY textChanged)

public:
    explicit MyWidget(QWidget *parent = nullptr);

    QString text() const;
    void setText(const QString &text);

signals:
    void textChanged();

private:
    QString m_text;
};

QString MyWidget::text() const
{
    return m_text;
}

void MyWidget::setText(const QString &text)
{
    if (text != m_text) {
        m_text = text;
        emit textChanged();
    }
}
```

此示例中声明了一个具有 `text` 属性的 `MyWidget` 类。使用 `Q_PROPERTY` 声明为只读或读/写属性。设置器方法应该在修改属性时发出对应的信号。

## Q_SIGNALS 和 Q_SLOTS

`Q_SIGNALS` 和 `Q_SLOTS` 宏分别用于声明信号和槽。这使得编译器能够在元对象中注册它们以进行运行时调用。例如：

```c++
class MyWidget : public QWidget
{
    Q_OBJECT

public:
    explicit MyWidget(QWidget *parent = nullptr);

signals:
    void buttonClicked();

private slots:
    void handleButton();
};
```

在此示例中，`MyWidget` 的 `buttonClicked()` 信号和 `handleButton()` 槽被声明为 `Q_SIGNALS` 和 `Q_SLOTS`。

## Q_EMIT 

`Q_EMIT` 宏用于发射信号。

```c++
void MyWidget::handleButton()
{
    // do something
    Q_EMIT buttonClicked();
}
```

## QT_VERSION_CHECK

`QT_VERSION_CHECK(major, minor, patch)` 用于在预处理期间检查 Qt 库版本。

```c++
#if QT_VERSION_CHECK(5, 14, 0)
// code for Qt 5.14.0 and later
#else
// code for earlier versions of Qt
#endif
```

## Q_DECL_OVERRIDE 和 Q_DECL_FINAL

`Q_DECL_OVERRIDE` 和 `Q_DECL_FINAL` 宏分别用于覆盖和禁止覆盖虚函数。

```c++
class MyWidget : public QWidget
{
    Q_OBJECT

public:
    explicit MyWidget(QWidget *parent = nullptr) {}

    virtual void paintEvent(QPaintEvent *event) Q_DECL_OVERRIDE;

    virtual void mousePressEvent(QMouseEvent *event) Q_DECL_FINAL;
};
```

## Q_DISABLE_COPY 和 Q_DISABLE_MOVE

`Q_DISABLE_COPY` 和 `Q_DISABLE_MOVE` 宏用于禁用类的默认拷贝构造函数和移动构造函数。这是为了防止代码复制和意外使用不安全的拷贝和移动函数。

```c++
class MyWidget : public QWidget
{
    Q_DISABLE_COPY(MyWidget)
    Q_DISABLE_MOVE(MyWidget)

public:
    explicit MyWidget(QWidget *parent = nullptr);
};
```

以上是常用的 Qt 内置宏，它们可以使 Qt 编程更加简洁和高效。希望本篇教程能够对您有所帮助！
