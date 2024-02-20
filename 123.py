import forms.main_form as main_form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QLabel)
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image, ImageFilter
import os

import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag




class my_Label(QLabel):

    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        QLabel.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print('press')

class Photo_Editor(QtWidgets.QMainWindow, main_form.Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        # self.button = Button('d', self)
        # self.button.move(100, 65)
        self.label_11 = my_Label('d', self.widget)
        # self.label_11.setText("")
        pixmap = QPixmap('test.jpg')

        self.label_11.setPixmap(pixmap)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.label_11.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Photo_Editor()
    window.show()
    app.exec_()
