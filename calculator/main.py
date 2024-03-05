from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from Layout import layout

if __name__ == "__main__":
    root = QApplication([])
    window = layout()
    window.setWindowIcon(QIcon("download.jpg"))
    root.exec()