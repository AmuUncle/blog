---
title: 使用Qt开发自定义委托的表格控件
date: 2021-10-20 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

# 使用Qt开发自定义委托的表格控件

在Qt中，可以使用自定义委托（QStyledItemDelegate）来实现自定义的表格控件，这个机制可以让开发者完全掌握表格单元格UI的显示方式和用户交互方式。

## 步骤一：设置表格模型

在创建表格前，需要先创建一个表格模型来存储数据。Qt中提供了QAbstractTableModel对象，其派生类可用于创建各种类型的表格模型，如列表、树状等，这里我们以一个简单的列表为例。

```cpp
class CustomTableModel : public QAbstractTableModel {
    Q_OBJECT
public:
    explicit CustomTableModel(QObject *parent = nullptr);

    int rowCount(const QModelIndex &parent) const override;
    int columnCount(const QModelIndex &parent) const override;
    QVariant data(const QModelIndex &index, int role) const override;
    bool setData(const QModelIndex &index, const QVariant &value, int role) override;

private:
    QList<QString> m_dataList;
};
```

以上代码定义了一个`CustomTableModel`类，为了展示文章重点在委托上，具体实现略去。

## 步骤二：自定义委托

自定义委托是实现表格控件的核心，而Qt中提供了QStyledItemDelegate对象作为实现基类，开发者通过继承直接派生此类并实现其中的四个虚函数以完成自定义：`paint()`、`createEditor()`、`setEditorData()` 和 `setModelData()`。

例如，以绘制自定义委托为例：

```cpp
class ColorDelegate : public QStyledItemDelegate {
public:
    explicit ColorDelegate(QObject *parent = nullptr);

private:
    void paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const override;
};
```

通过`paint()`方法，可以实现对单元格的绘制方式，以下是一个简单的例子：

```cpp
void ColorDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    painter->save();
    painter->setRenderHint(QPainter::Antialiasing);
    painter->setPen(Qt::NoPen);
    painter->setBrush(QColor("#FF0000"));
    painter->drawRect(option.rect);

    painter->restore();
}
```

上述代码的作用是：将单元格绘制成红色矩形。

## 步骤三：设置委托

一旦创建了自定义委托对象以后，需要将委托对象设置到表格控件中，从而绑定自定义单元格的显示方式和用户交互方式。

在Qt中，通过表格模型的setItemDelegate()方法即可将自定义委托设置到表格中：

```cpp
ui->tableView->setItemDelegate(new ColorDelegate(this));
```

以上代码将刚刚创建的红色单元格样式代理設置给表格。

## 总结

使用自定义委托来实现表格控件可以让开发者完全掌握单元格UI的显示方式和用户交互方式。在具体实现过程中，需要了解表格模型和委托类的具体用法，并重载QStyledItemDelegate的四个虚函数。
