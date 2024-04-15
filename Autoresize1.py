from PyQt5.QtGui import QPixmap,QPainter
import sys
from PyQt5 import *

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication


class Label(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = QPixmap()

    def setPixmap(self, p):
        self.p = p
        self.update()

    def paintEvent(self, event):
        if not self.p.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.p)


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        lay = (self)
        lb = Label(self)
        lb.setPixmap(QPixmap(r"C:\Users\Admin\PythonLession\pic\geeksforgeeks.png"))





app = QApplication(sys.argv)
w = Widget()
w.show()
sys.exit(app.exec_())