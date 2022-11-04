# 1.1 Basics
- pyqt is a library for creating GUI applications based on the QT framework
- pyqt is released under the GPL license
- link to the pyqt documentation for widgets: [link](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtwidgets-module.html)
- llink to the reference of pyqt: [link](https://www.riverbankcomputing.com/static/Docs/PyQt5/))


# 1.2 Concepts
- py qt separates the functionality into different modules
    - **Qtcore**: core non-GUI
    - **QtGui**: windowmanagement like event handling and graphics
    - **QtWidgets**: widgets of the QT framework, e.g. buttons, labels, textinputs, ...
    - **QtMultimedia**: functionality for multimedia content
    - **QtBluetooth**: bluetooth functionality
    - **QtNetwork**: socket/server functionality (tcp/ip and UDP)
    - **QtPositioning**: global position functionality (gps, ...)
    - **QtWebSocket**: websocket protocol
    - **QtWebKit**: implementation of the *"WebKit2"* framework, e.g. rendering of websites
    - **QtWebKitWidgets**: **DEPRECATED** older webkit implementation
    - **QtXML**: xml Parser
    - **QtSvg**: functionality to process **S**calable**V**ector**G**raphics
    - **QtSql**: sql functionality
    - **QtTest**: unit tests
- the base of any Qt Application is the PyQt[n].QtWidgets.QApplication object, it handles the ui-loop
- every ui-element in PyQt has the base PyQt[n].QtWidgets.QWidget
> means all Widgets share a common interface to set general attributes
