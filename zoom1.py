from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self, *args):
        super().__init__(*args)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button_zoom_in = QPushButton('Zoom IN', self)
        self.button_zoom_in.clicked.connect(self.on_zoom_in)
        self.layout.addWidget(self.button_zoom_in)

        self.button_zoom_out = QPushButton('Zoom OUT', self)
        self.button_zoom_out.clicked.connect(self.on_zoom_out)
        self.layout.addWidget(self.button_zoom_out)

        self.pixmap = QPixmap(r'C:\Users\Admin\PythonLession\CarPlate\images\BSXe_tested\0144_00471_b.jpg')
        self.height = self.pixmap.height()

        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.layout.addWidget(self.label)

        self.show()

    def on_zoom_in(self, event):
        self.height += 100
        self.resize_image()

    def on_zoom_out(self, event):
        self.height -= 100
        self.resize_image()

    def resize_image(self):
        scaled_pixmap = self.pixmap.scaledToHeight(self.height)
        self.label.setPixmap(scaled_pixmap)

# --- main ---
if __name__ == '__main__':

    app = QApplication([])
    win = MyApp()
    app.exec()