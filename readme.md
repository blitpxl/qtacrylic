# About
qtacrylic is a python module to apply Windows 10's Acrylic Material Theme onto a PyQt/PySide window.

You can also apply the Aero Material Theme using this module.

# Issue with newer version of windows

If you're running a Windows version above 1809, and trying to apply the acrylic material, then you will be very likely
to encounter a bug where the window lags behind the cursor when you resize/move the window. Fortunately this bug is only occured
with the Acrylic blur. Meaning you can still use the Aero blur without problem. 

This bug is located in windows' dwm (desktop window manager), meaning we couldn't do anything to completely mitigate the issue, 
we have to wait the Windows developers to fix the bug.
There's however a very crude and temporary fix to this problem by disabling Acrylic shadow and adding a delay when you resize/move the window:

```python
    def moveEvent(self, event) -> None:
        time.sleep(0.02)  # sleep for 20ms

    def resizeEvent(self, event) -> None:
        time.sleep(0.02)  # sleep for 20ms
```

This may introduce a noticeably minor stutter or unsmooth window moving/resizing.

# How to use it

Import the module:
```python
from qtacrylic import WindowEffect
```

An example code of how to apply the material:

```python
from PySide2.QtWidgets import QWidget, QApplication
from qtacrylic import WindowEffect  # import the module
from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedWidth(400)  # set a fixed width for the window
        self.setFixedHeight(400)  # set a fixed height for the window

        self.setWindowFlags(Qt.FramelessWindowHint)  # make the window frameless
        self.setAttribute(Qt.WA_TranslucentBackground)  # make the window translucent

        self.ui_layout = QtWidgets.QGridLayout(self)  # create a ui layout
        self.ui_layout.setAlignment(Qt.AlignCenter)  # center the layout

        self.label = QtWidgets.QLabel("Hello World!", self)  # create a label to display a text
        self.label.setFont(QFont("Segoe UI", 14))  # configure the text size and font
        self.ui_layout.addWidget(self.label)  # add the label widget into the layout

        self.windowFX = WindowEffect()  # instatiate the WindowEffect class
        self.windowFX.setAcrylicEffect(self.winId())  # set the Acrylic effect by specifying the window id


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    app.exec_()
```

![](https://i.ibb.co/GVcWbS5/acrylic.png)

To apply the Aero effect simply replace `setAcrylicEffect()` with `setAeroEffect()`
```python
self.windowFX = WindowEffect()  # instatiate the WindowEffect class
self.windowFX.setAeroEffect(self.winId())  # set the Aero effect by specifying the window id
```
![](https://i.ibb.co/YbStDkQ/aero.png)
