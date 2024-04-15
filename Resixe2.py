from PyQt5 import QtCore, QtGui, QtWidgets
from itertools import cycle
from glob import glob

class Label(QtWidgets.QLabel):
    def resizeEvent(self, event):
        if not hasattr(self, 'maximum_size'):
            self.maximum_size = self.size()
        else:
            self.maximum_size = QtCore.QSize(
                max(self.maximum_size.width(), self.width()),
                max(self.maximum_size.height(), self.height()),
            )
        super(Label, self).resizeEvent(event)

    def setPixmap(self, pixmap):
        scaled = pixmap.scaled(self.maximum_size, QtCore.Qt.KeepAspectRatio)
        super(Label, self).setPixmap(scaled)

class Demo(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowState(QtCore.Qt.WindowMaximized)
        layout = QtWidgets.QVBoxLayout(self)
        self.button = QtWidgets.QPushButton("Next image")
        self.label = Label()
        self.label.setStyleSheet("QLabel { background-color : red; }")
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.showImage)
        self.show()
        self.images = cycle(glob('C:/Users/Admin/PythonLession/CarPlate/images/BSXe_tested/*.jpg'))

    def showImage(self):
        try:
            filename = next(self.images)
            self.label.setPixmap(QtGui.QPixmap(filename))
            sp = self.label.sizePolicy()
            sp.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
            self.label.setSizePolicy(sp)
            self.layout().setAlignment(self.label, QtCore.Qt.AlignCenter)
        except StopIteration:
            pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = Demo()
    sys.exit(app.exec_())