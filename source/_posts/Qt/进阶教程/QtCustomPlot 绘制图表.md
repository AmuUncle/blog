---
title: QtCustomPlot 绘制图表
date: 2021-11-22 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

# 使用 QtCustomPlot 绘制图表

## 介绍

QtCustomPlot 是一个基于 Qt 的图表库，用于创建数据可视化图表。它支持多种类型的图表，包括折线图、散点图、柱状图等，并提供了多种自定义选项，以便用户对其外观和行为进行优化。

在本教程中，我们将向您展示如何使用 QtCustomPlot 来创建一个简单的折线图来可视化数据。

## 准备工作

在开始之前，请确保已满足以下要求：

1. 安装了 Qt 5 或更高版本。
2. 下载并安装了 QtCustomPlot 库。
   - 您可以在[此处](https://github.com/qtcustomplot/qtcustomplot/releases)下载最新版本的库。
3. 创建一个新的 Qt 项目，在 `.pro` 文件中添加以下行以引用 QtCustomPlot 库：
   ```
   include(path/to/qtcustomplot.pri)
   ```

## 步骤

1. 定义一个 `QCustomPlot` 对象，该对象将承载我们的图表。
   ```
   QCustomPlot *customPlot = new QCustomPlot(this);
   ```
2. 创建一个称为“图形”（graph）的对象，用于在图表中显示数据。
   ```
   QCPGraph *graph = customPlot->addGraph();
   ```
3. 将数据添加到图形对象中，以便在图表中显示。
   ```
   QVector<double> xData, yData;
   // 添加您的数据到 xData 和 yData 向量中
   graph->setData(xData, yData);
   ```
4. （可选） 设置轴的标签和范围。
   ```
   customPlot->xAxis->setLabel("X Axis");
   customPlot->yAxis->setLabel("Y Axis");
   customPlot->xAxis->setRange(0, 10);
   customPlot->yAxis->setRange(0, 100);
   ```
5. 显示图表。
   ```
   customPlot->replot();
   ```

## 示例代码

完整示例代码如下所示：

```
#include <QtCustomPlot/QCustomPlot>

QCustomPlot *customPlot = new QCustomPlot(this);

QCPGraph *graph = customPlot->addGraph();

QVector<double> xData, yData;
// 添加您的数据到 xData 和 yData 向量中
graph->setData(xData, yData);

customPlot->xAxis->setLabel("X Axis");
customPlot->yAxis->setLabel("Y Axis");

customPlot->xAxis->setRange(0, 10);
customPlot->yAxis->setRange(0, 100);

customPlot->replot();
```

以上就是使用 `QtCustomPlot` 绘制图表的基本步骤，您可以根据需要自定义更多样式和外观选项。