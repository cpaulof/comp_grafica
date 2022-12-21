import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)

from main_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())