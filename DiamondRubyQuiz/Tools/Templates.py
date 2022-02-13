from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class AnimatedButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(120, 30)

        self.color1 = QColor(240, 53, 218)
        self.color2 = QColor(61, 217, 245)
        self._animation = QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250,
        )

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI"; 
        	font-weight: bold; 
            text-align: center;
        	color: rgb(255, 255, 255); 
        	border-style: solid; 
            padding: 5px;
        	border-radius:10px; 
        	"""
        grad = f"""
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {self.color1.name()}, stop:{value} {self.color2.name()}, stop: 1.0 {self.color1.name()}
                )
            """

        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)


class OptionButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(120, 30)

        self.color1 = QColor(240, 53, 218)
        self.color2 = QColor(61, 217, 245)
        self._animation = QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250,
        )

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI"; 
            font-weight: bold; 
            text-align: left;
            color: rgb(255, 255, 255); 
            border-style: solid; 
            padding: 5px;
            border-radius:10px; 
            """
        grad = """
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1}
                )
            """.format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)


class SwitchButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        qss = """
        QPushButton {
            font: 75 10pt "Microsoft YaHei UI"; 
            font-weight: bold; 
            text-align: center;
            color: rgb(255, 255, 255); 
            border-style: solid;
            border: 1px solid rgb(240, 53, 180);
            padding: 5px;
            border-radius:10px;
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(240, 53, 218), stop:1 rgb(61, 217, 245)
                )
            }
        QPushButton:hover {
            background-color: rgb(240, 53, 218);
            }
            """

        self.setStyleSheet(qss)


class QuestionButton(QPushButton):
    def __init__(self, text, widget):
        QPushButton.__init__(self)

        self.text = text
        self.widget = widget

        qss = """
        QPushButton {
            font: 75 10pt "Microsoft YaHei UI"; 
            font-weight: bold; 
            text-align: center;
            color: rgb(255, 255, 255); 
            border-style: solid;
            border: 1px solid rgb(240, 53, 180);
            padding: 5px;
            border-radius:10px;
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(240, 53, 218), stop:1 rgb(61, 217, 245)
                )
            }
        QPushButton:hover {
            background-color: rgb(240, 53, 218);
            }
            """

        self.setStyleSheet(qss)
        self.setText(str(self.text))
        self.clicked.connect(self.slot)

    def slot(self):
        self.widget.setCurrentIndex(int(self.text) - 1)
