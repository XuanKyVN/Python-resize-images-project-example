from PyQt5 import QtCore, QtGui, QtWidgets

class Demo(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowState(QtCore.Qt.WindowMaximized)
        layout = QtWidgets.QVBoxLayout(self)
        self.button = QtWidgets.QPushButton("Next image")
        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet("QLabel { background-color : red; }")
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.showImage)
        self.show()

    def showImage(self):
        self.pixmap = QtGui.QPixmap(r'C:\Users\Admin\PythonLession\CarPlate\images\BSXe_tested\0144_00471_b.jpg')
        scaled = self.pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(scaled)
        sp = self.label.sizePolicy()
        sp.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        self.label.setSizePolicy(sp)
        self.layout().setAlignment(self.label, QtCore.Qt.AlignCenter)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = Demo()
    sys.exit(app.exec_())