---
title: 什么是QWebEngineView和QWebChannel？
date: 2021-11-24 11:34:06
categories: 
    - Qt进阶教程
tags: Qt
---

当您准备开发一个现代化的Web应用程序时，QWebEngineView和QWebChannel是两个重要的Qt组件。这篇博客将会给您介绍它们的用途，以及如何在您的Qt代码中使用它们。

## QWebEngineView是什么？

QWebEngineView是一个基于Chromium引擎的Qt组件，用于呈现和交互Web页面。当您需要在Qt应用程序中嵌入Web内容时，QWebEngineView会很有用。它提供了一些便利的方法来加载、导航和操作Web页面，比如：

```cpp
QWebEngineView *view = new QWebEngineView(this);
view->load(QUrl("https://www.example.com"));
```

以上代码创建了一个QWebEngineView对象，并通过`load`方法将其载入指定的URL。如果您希望捕获Web页面的截图或输出HTML源代码等操作，QWebEngineView也提供了相应的API实现。

## QWebChannel是什么？

QWebChannel是另一个Qt组件，它提供了一种简单的机制来在Web页面和Qt应用程序之间进行通信。在使用QWebChannel时，您可以从JavaScript代码中调用Qt对象的方法，或者通过Qt对象接收来自Web页面的事件和数据。

为了使用QWebChannel，您需要执行以下步骤：

1. 将一个QWebChannel对象附加到QWebEngineView上。
2. 在Qt代码中声明一个QObject派生类，并使用`QWebChannel::registerObject`方法将其注册到QWebChannel对象中。
3. 在Web页面中，使用`qt.webChannelTransport`对象来连接到QWebChannel，并通过`qt.webChannel.objects`数组访问已注册的Qt对象。

以下是一个简单的代码示例，展示了如何在Qt应用程序和Web页面之间交换数据：

**main.cpp**
```cpp
#include <QApplication>
#include <QDebug>
#include <QObject>
#include <QWebEngineView>
#include <QWebChannel>

class MyObject : public QObject
{
    Q_OBJECT

public slots:
    void onMessage(const QString &message)
    {
        qDebug() << "Received message from web page:" << message;
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    // 创建QWebEngineView对象并添加到主窗口中
    QWebEngineView *view = new QWebEngineView();
    view->setUrl(QUrl("qrc:///index.html"));

    // 创建QWebChannel对象并附加到QWebEngineView对象上
    QWebChannel *channel = new QWebChannel(view);
    view->page()->setWebChannel(channel);

    // 在Qt代码中创建MyObject对象，并将其注册到QWebChannel对象中
    MyObject myObject;
    channel->registerObject(QStringLiteral("myObject"), &myObject);

    view->show();
    return app.exec();
}

#include "main.moc"
```

**index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>QWebChannel Example</title>
</head>
<body>
    <h1>QWebChannel Example</h1>
    <button onclick="sendMessage()">Send Message to Qt</button>
    <script type="text/javascript" src="qrc:///qtwebchannel/qwebchannel.js"></script>
    <script type="text/javascript">
        // 连接到QWebChannel并获取已注册的Qt对象
        var webChannel = new QWebChannel(qt.webChannelTransport, function(channel) {
            var myObject = channel.objects.myObject;

            // 在点击按钮时调用MyObject对象的onMessage方法
            function sendMessage() {
                myObject.onMessage("Hello from Web");
            }
        });
    </script>
</body>
</html>
```

在这个例子中，我们创建了一个名为`MyObject`的QObject派生类，并将其注册到了一个名为`myObject`的对象名上。Web页面中的JavaScript代码使用`qt.webChannelTransport`连接到了QWebChannel，然后通过`qt.webChannel.objects.myObject`访问了已注册的Qt对象。当点击按钮时，Web页面上的JavaScript调用了`myObject.onMessage("Hello from Web")`，这个调用会触发Qt对象中的`onMessage`方法，并输出一条消息到控制台。

## 在QWebEngineView中使用QWebChannel

在上面的例子中，我们演示了如何使用QWebChannel在Qt应用程序和Web页面之间交换数据。现在，让我们看看如何在QWebEngineView中使用QWebChannel来控制Web页面的行为。

首先，我们需要创建一个新的QObject派生类，以便将其注册到QWebChannel中：

```cpp
class WebController : public QObject
{
    Q_OBJECT

public slots:
    void setButtonStyle(const QString &style);
    void setLabelStyle(const QString &style);

private:
    QWebEnginePage *m_page;
};
```

这里，我们声明了两个槽函数：`setButtonStyle`和`setLabelStyle`。这些槽函数将通过QWebChannel暴露给Web页面的JavaScript代码。我们还添加了一个指向`QWebEnginePage`对象的指针，这样我们就可以从槽函数中直接操作Web页面了。

我们的下一步是将这个新对象注册到QWebChannel中：

```cpp
QWebChannel *channel = new QWebChannel(view->page());
WebController *controller = new WebController();
controller->setPage(view->page());
channel->registerObject(QStringLiteral("webController"), controller);
```

在这个例子中，我们将`WebController`对象注册为`webController`对象，然后将其附加到了QWebChannel对象中。

现在，我们需要在Web页面中添加一些JavaScript代码来连接到QWebChannel，并使用`webController`对象。这里是一个例子：

```javascript
new QWebChannel(qt.webChannelTransport, function (channel) {
    var webController = channel.objects.webController;
    webController.setButtonStyle("background-color: blue; color: white;");
    webController.setLabelStyle("font-weight: bold;");
});
```

在这个例子中，我们在QWebChannel对象上创建了一个新的JavaScript对象，并通过`channel.objects.webController`访问了已经注册的`WebController`对象。然后，我们调用了`setButtonStyle`和`setLabelStyle`槽函数，从而改变了Web页面上的按钮和标签样式。

## 结论

在这篇博客中，我们介绍了Qt框架中两个非常有用的组件：QWebEngineView和QWebChannel。QWebEngineView可以帮助您将Web内容嵌入到您的Qt应用程序中，而QWebChannel则允许您在Qt代码和Web页面之间交换数据。这些组件非常容易使用，而且可以帮助您构建出更加现代化、功能更加强大的Qt应用程序。

除了上述提到的基本使用方法，QWebEngineView和QWebChannel还有许多其他使用技巧和注意事项。下面是一些需要特别注意的问题：

- 在Qt5.6及更高版本中，QWebChannel已经被移动到了QtWebChannel库中。因此，在使用QWebChannel时，需要在.pro文件中添加`QT += webchannel`。

- 建议不要将QWebEngineView对象和QWebChannel对象的生命周期直接绑定在某个特定的QWidget或QObject对象上。如果必须这样做，请确保在销毁父对象之前先销毁QWebEngineView和QWebChannel对象。

- 可以考虑使用JavaScript Promise API来管理复杂的异步操作。例如，在加载Web页面时，我们可以使用Promise API来等待页面加载完成后再执行后续操作。

- 如果Web页面需要与外部服务进行交互（例如通过AJAX请求数据），则可以使用Qt框架中提供的网络API来实现。

- 如果需要在Web页面中使用一些第三方JavaScript库（例如jQuery、React等），则可以将这些库作为静态资源打包到Qt应用程序中，并使用`qrc:` URL来引用。

总而言之，QWebEngineView和QWebChannel为开发人员提供了强大而灵活的工具来构建现代化的Qt应用程序。无论您是想要嵌入Web内容，还是需要在Qt代码和Web页面之间交换数据，QWebEngineView和QWebChannel都可以帮助您轻松实现。
## 完整代码示例

最后，这里是一个完整的代码示例，演示了如何在Qt应用程序中使用QWebEngineView和QWebChannel。这个例子包含了三个文件：

- `main.cpp`：应用程序入口，创建主窗口并加载Web页面。
- `webcontroller.h`和`webcontroller.cpp`：定义了`WebController`类，它是我们向QWebChannel注册的QObject派生类。

**main.cpp**
```cpp
#include <QApplication>
#include <QDebug>
#include <QObject>
#include <QWebEngineView>
#include <QWebChannel>

#include "webcontroller.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    // 创建QWebEngineView对象并添加到主窗口中
    QWebEngineView *view = new QWebEngineView();
    view->setUrl(QUrl("qrc:///index.html"));

    // 创建QWebChannel对象并附加到QWebEngineView对象上
    QWebChannel *channel = new QWebChannel(view->page());
    WebController *controller = new WebController();
    controller->setPage(view->page());
    channel->registerObject(QStringLiteral("webController"), controller);
    view->page()->setWebChannel(channel);

    view->show();
    return app.exec();
}
```

**webcontroller.h**
```cpp
#ifndef WEBCONTROLLER_H
#define WEBCONTROLLER_H

#include <QObject>
#include <QWebEnginePage>

class WebController : public QObject
{
    Q_OBJECT

public slots:
    void setButtonStyle(const QString &style);
    void setLabelStyle(const QString &style);

private:
    QWebEnginePage *m_page;
};

#endif // WEBCONTROLLER_H
```

**webcontroller.cpp**
```cpp
#include "webcontroller.h"

void WebController::setButtonStyle(const QString &style)
{
    m_page->runJavaScript(QString("document.getElementById('myButton').style='%1'").arg(style));
}

void WebController::setLabelStyle(const QString &style)
{
    m_page->runJavaScript(QString("document.getElementById('myLabel').style='%1'").arg(style));
}

void WebController::setPage(QWebEnginePage *page)
{
    m_page = page;
}
```

**index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>QWebChannel Example</title>
</head>
<body>
    <h1>QWebChannel Example</h1>
    <button id="myButton" onclick="sendMessage()">Send Message to Qt</button>
    <br><br>
    <label id="myLabel">This is a label</label>
    <br><br>
    <input type="text" id="myInput">
    <br><br>
    <script type="text/javascript" src="qrc:///qtwebchannel/qwebchannel.js"></script>
    <script type="text/javascript">
        // 连接到QWebChannel并获取已注册的Qt对象
        new QWebChannel(qt.webChannelTransport, function (channel) {
            var webController = channel.objects.webController;
            webController.setButtonStyle("background-color: blue; color: white;");
            webController.setLabelStyle("font-weight: bold;");

            // 当点击按钮时，调用MyObject对象的onMessage方法
            function sendMessage() {
                var inputValue = document.getElementById("myInput").value;
                alert("You entered: " + inputValue);
            }
        });
    </script>
</body>
</html>
```

在这个例子中，我们创建了一个简单的Web页面，其中包含一个按钮、一个标签和一个文本框。当用户点击按钮时，JavaScript代码会通过QWebChannel对象调用`setButtonStyle`和`setLabelStyle`方法，从而改变按钮和标签的样式。同时，JavaScript代码还会弹出一个对话框，显示用户在文本框中输入的内容。

总之，QWebEngineView和QWebChannel是非常有用的Qt组件，它们可以帮助您构建出现代化、功能丰富的Qt应用程序，让您的应用程序更加灵活、可扩展。

## 参考资料

如果您想了解更多关于QWebEngineView和QWebChannel的信息，可以参考以下官方文档：

- [Qt WebEngine](https://doc.qt.io/qt-5/qtwebengine-index.html)
- [Qt WebChannel](https://doc.qt.io/qt-5/qtwebchannel-index.html)

此外，以下是一些其他有用的资源：

- [QWebEngineView实现Qt与Web的交互](https://www.cnblogs.com/QtXiaoBei/p/12263885.html)
- [Using QWebChannel to expose C++ objects to JavaScript](https://doc.qt.io/qt-5/qtwebchannel-javascriptexample.html)
- [Creating a simple browser with QtWebEngine](https://blog.qt.io/blog/2016/06/10/creating-a-simple-browser-with-qtwebengine/)
- [Integrating HTML and QML Using the Qt WebEngine](https://doc.qt.io/qt-5/qtwebengine-webengineqml-example.html)

通过这些资料，您可以深入了解如何在Qt应用程序中使用QWebEngineView和QWebChannel，并学习如何构建出现代化、功能丰富的Qt应用程序。

## 总结

在本篇博客中，我们介绍了Qt框架中两个非常有用的组件：QWebEngineView和QWebChannel。QWebEngineView可以帮助您将Web内容嵌入到您的Qt应用程序中，而QWebChannel则允许您在Qt代码和Web页面之间交换数据。

我们首先演示了如何使用QWebEngineView在Qt应用程序中加载Web页面，并且如何利用JavaScript代码与页面进行交互。然后，我们介绍了如何使用QWebChannel实现Qt代码与Web页面之间的双向通信，从而使得应用程序更加灵活、可扩展。

最后，我们提供了一个完整的代码示例，演示了如何在Qt应用程序中使用QWebEngineView和QWebChannel。通过这个例子，您可以深入了解QWebEngineView和QWebChannel的使用方法，并学习如何构建出现代化、功能丰富的Qt应用程序。

希望本篇博客能够对您有所帮助！
