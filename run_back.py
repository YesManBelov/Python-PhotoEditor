import forms.main_form as main_form
import forms.question as question
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QLabel, QWidget)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QIcon, QPixmap, QDrag
from PIL import Image, ImageFilter, ImageOps
import os

class Question(QtWidgets.QMainWindow, question.Ui_MainWindow):
    def __init__(self, ob):
        super().__init__()
        self.ob = ob
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.sbros)

    def sbros(self):
        self.ob.huy()
        self.close()


## ошибка в условиях
class my_Label(QLabel):
    '''нужен для двигателя изображения'''

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
        # label:
        self.window_q = None
        self.setAcceptDrops(True)
        self.label_11 = my_Label('d', self.widget)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 691, 671))
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_11.setMouseTracking(True)
        self.label_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        # label end

        self.but_15_names = ['Вернуть изменения']
        self.block = False
        self.action_6.triggered.connect(self.open_file)
        self.action_9.triggered.connect(self.save_file)
        self.action_10.triggered.connect(self.save_how_file)
        self.action_12.triggered.connect(exit)
        self.action_13.triggered.connect(self.questions)
        self.action_15.triggered.connect(self.all_clear)
        self.action_24.triggered.connect(self.convert_flip_vertical)
        self.action_25.triggered.connect(self.convert_flip_horisontal)
        self.action_26.triggered.connect(self.filter_b_w)
        self.action_27.triggered.connect(self.filter_blur)
        self.action_28.triggered.connect(self.filter_non_colors)
        self.action_29.triggered.connect(self.filter_sepia)
        self.action_30.triggered.connect(self.filter_pseudo)
        self.action_31.triggered.connect(self.filter_negative)
        self.action_32.triggered.connect(self.filter_r)
        self.action_33.triggered.connect(self.filter_g)
        self.action_34.triggered.connect(self.filter_b)
        self.action90.triggered.connect(self.convert_to_90_r)
        self.action90_2.triggered.connect(self.convert_to_90_l)
        self.action180.triggered.connect(self.convert_to_180)
        self.pushButton.clicked.connect(self.filter_b_w)
        self.pushButton_2.clicked.connect(self.filter_blur)
        self.pushButton_3.clicked.connect(self.filter_non_colors)
        self.pushButton_4.clicked.connect(self.filter_negative)
        self.pushButton_5.clicked.connect(self.filter_sepia)
        self.pushButton_6.clicked.connect(self.filter_pseudo)
        self.pushButton_7.clicked.connect(self.filter_r)
        self.pushButton_8.clicked.connect(self.filter_g)
        self.pushButton_9.clicked.connect(self.filter_b)
        self.pushButton_10.clicked.connect(self.plus_img)
        self.pushButton_19.clicked.connect(self.minus_img)
        self.pushButton_11.clicked.connect(self.b_c_DEactivate)
        self.pushButton_12.clicked.connect(self.autobringless)
        self.pushButton_13.clicked.connect(self.autocontrast)
        self.pushButton_14.clicked.connect(self.auto_color)
        self.pushButton_15.clicked.connect(self.paint_original)
        self.pushButton_16.clicked.connect(self.questions)
        self.pushButton_17.clicked.connect(self.all_clear)
        self.pushButton_18.clicked.connect(self.b_c_activate)
        self.horizontalSlider.valueChanged.connect(self.slider_1)
        self.horizontalSlider_2.valueChanged.connect(self.slider_2)
        self.start()

    def huy(self):
        print('huy')
        self.start()
        print('k')
        self.label_11.clear()

    def plus_img(self):
        x = self.label_11.x()
        y = self.label_11.y()
        width = self.label_11.width()
        height = self.label_11.height()

        self.koef += 15
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg', True, 'up')
        self.label_11.setGeometry(QtCore.QRect(x, y, width+15, height+15))

    def minus_img(self):
        self.koef -= 15
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg', True, 'down')

    def dragEnterEvent(self, e):
        e.accept()
        self.start_position = e.pos()
        print('back', self.start_position)
        self.label_x = self.label_11.x()
        self.label_y = self.label_11.y()
        self.label_width = self.label_11.width()
        self.label_height = self.label_11.height()
        print('dd')

    def dropEvent(self, e):
        position = e.pos()
        print('zzz', self.start_position)
        x = position.x() - self.start_position.x()
        y = position.y() - self.start_position.y()
        print('end', position)
        self.label_11.setGeometry(QtCore.QRect(self.label_x + x, self.label_y + y, self.label_width, self.label_height))

        e.setDropAction(Qt.MoveAction)
        e.accept()

    def convert_flip_vertical(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        self.post_image = self.post_image.transpose(Image.FLIP_TOP_BOTTOM)
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')

    def convert_flip_horisontal(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        self.post_image = self.post_image.transpose(Image.FLIP_LEFT_RIGHT)
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')

    def convert_to_90_r(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        self.post_image = self.post_image.rotate(-90)
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')

    def convert_to_90_l(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        self.post_image = self.post_image.rotate(90)
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')

    def convert_to_180(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        self.post_image = self.post_image.rotate(180)
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')

    def all_clear(self):
        self.b_c_DEactivate()
        self.paint_image(self.hidden_name)

    def questions(self):
        self.window_q = Question(self)
        self.window_q.show()


    def start(self):
        self.koef = 0
        # label:
        self.label_11.clear()
        self.label_11.setGeometry(QtCore.QRect(0, 0, 691, 671))
        # label end
        self.b_c_DEactivate()
        self.textEdit.setEnabled(False)
        self.textEdit_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.pushButton_19.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider_2.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.action_10.setEnabled(False)
        self.action_9.setEnabled(False)
        self.menu_2.setEnabled(False)
        self.menu_3.setEnabled(False)

    def open_blocks(self):
        self.b_c_DEactivate()
        self.textEdit.setEnabled(True)
        self.textEdit_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.pushButton_17.setEnabled(True)
        self.pushButton_18.setEnabled(True)
        self.pushButton_19.setEnabled(True)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider_2.setEnabled(True)
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.action_10.setEnabled(True)
        self.action_9.setEnabled(True)
        self.menu_2.setEnabled(True)
        self.menu_3.setEnabled(True)

    def paint_original(self):
        self.b_c_DEactivate()
        self.but_15_names.append(self.pushButton_15.text())
        self.pushButton_15.setText(self.but_15_names.pop(0))
        if self.pushButton_15.text() == 'Вернуть изменения':
            self.block = True
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.pushButton_9.setEnabled(False)
            self.pushButton_10.setEnabled(False)
            self.pushButton_11.setEnabled(False)
            self.pushButton_12.setEnabled(False)
            self.pushButton_13.setEnabled(False)
            self.pushButton_14.setEnabled(False)
            self.pushButton_16.setEnabled(False)
            self.pushButton_17.setEnabled(False)
            self.pushButton_18.setEnabled(False)
            self.pushButton_19.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.horizontalSlider_2.setEnabled(False)
            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.paint_image(self.hidden_name, True)
        else:
            self.block = False
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_6.setEnabled(True)
            self.pushButton_7.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.pushButton_9.setEnabled(True)
            self.pushButton_10.setEnabled(True)
            self.pushButton_11.setEnabled(True)
            self.pushButton_12.setEnabled(True)
            self.pushButton_13.setEnabled(True)
            self.pushButton_14.setEnabled(True)
            self.pushButton_16.setEnabled(True)
            self.pushButton_17.setEnabled(True)
            self.pushButton_18.setEnabled(True)
            self.pushButton_19.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
            self.horizontalSlider_2.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.paint_image(self.redactor_name)

    def b_c_DEactivate(self):
        self.horizontalSlider.setValue(0)
        self.horizontalSlider_2.setValue(0)

    def b_c_activate(self):
        self.pushButton_15.setEnabled(True)
        self.paint_image('temps/test3.jpg')
        self.horizontalSlider.setValue(0)
        self.horizontalSlider_2.setValue(0)

    def autobringless(self):
        '''авто-яркость'''
        self.pushButton_15.setEnabled(True)
        hidden_paint = self.post_image
        def contrast(c):
            value = c+2
            return value

        hidden_paint = hidden_paint.point(contrast)
        hidden_paint.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        self.pushButton_12.setEnabled(False)

    def autocontrast(self):
        '''авто-контрас'''
        self.pushButton_15.setEnabled(True)
        hidden_paint = self.post_image
        factor = (259 * (20 + 255)) / (255 * (259 - 20))
        print(factor)

        def contrast(c):
            value = 128 + factor * (c - 128)
            print('value:', value)
            return max(0, min(255, value))

        hidden_paint = hidden_paint.point(contrast)
        hidden_paint.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg', True)
        self.pushButton_13.setEnabled(False)

    def auto_color(self):
        '''авто-цвет'''
        self.pushButton_15.setEnabled(True)
        factor = (259 * (20 + 255)) / (255 * (259 - 20))
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        self.pushButton_14.setEnabled(False)

    def slider_1(self):
        self.pushButton_15.setEnabled(True)
        hidden_paint = self.post_image
        level = self.horizontalSlider.value()
        self.textEdit.setText(str(level))

        def contrast(c):
            value = c + level
            return value

        hidden_paint = hidden_paint.point(contrast)
        hidden_paint.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg', True)

    def slider_2(self):
        self.pushButton_15.setEnabled(True)
        hidden_paint = self.post_image
        level = self.horizontalSlider_2.value()
        self.textEdit_2.setText(str(level))
        factor = (259 * (level + 255)) / (255 * (259 - level))
        print(factor)

        def contrast(c):
            value = 128 + factor * (c - 128)
            print('value:', value)
            return max(0, min(255, value))

        hidden_paint = hidden_paint.point(contrast)
        hidden_paint.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg', True)

    def filter_pseudo(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        from colorsys import hsv_to_rgb

        def pseudocolor(val, minval, maxval):
            h = (float(val - minval) / (maxval - minval)) * 120
            r, g, b = hsv_to_rgb(h / 360, 1., 1.)
            return r, g, b

        self.post_image = self.post_image.convert('RGB')
        for i in range(0, self.post_image.size[0] - 1):
            for j in range(0, self.post_image.size[1] - 1):
                r, g, b = self.post_image.getpixel((i, j))
                r, g, b = pseudocolor(r, 0, 100)
                r = int(r * 255)
                g = int(g * 255)
                b = int(b * 255)
                self.post_image.putpixel((i, j), (r, g, b))
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')

    def filter_blur(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        self.post_image = self.post_image.filter(ImageFilter.GaussianBlur(20))
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        return

    def filter_r(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        for i in range(0, self.post_image.size[0] - 1):
            for j in range(0, self.post_image.size[1] - 1):
                pixel_color = self.post_image.getpixel((i, j))
                r = pixel_color[0]
                self.post_image.putpixel((i, j), (r, 0, 0))
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        return

    def filter_g(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        for i in range(0, self.post_image.size[0] - 1):
            for j in range(0, self.post_image.size[1] - 1):
                pixel_color = self.post_image.getpixel((i, j))
                g = pixel_color[1]
                self.post_image.putpixel((i, j), (0, g, 0))
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        return

    def filter_b(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        for i in range(0, self.post_image.size[0] - 1):
            for j in range(0, self.post_image.size[1] - 1):
                pixel_color = self.post_image.getpixel((i, j))
                b = pixel_color[2]
                self.post_image.putpixel((i, j), (0, 0, b))
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        return

    def filter_negative(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()

        def contrast(c):
            value = 255 - c
            return value

        self.post_image = self.post_image.point(contrast)
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        print('применяю негатив')

    def filter_non_colors(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        self.post_image = self.post_image.convert('L')
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        return

    def filter_sepia(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        depth = 30
        for i in range(0, self.post_image.size[0] - 1):
            for j in range(0, self.post_image.size[1] - 1):
                r, g, b = self.post_image.getpixel((i, j))
                S = (r + g + b) // 3
                r = S + depth * 2
                g = S + depth
                b = S
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                self.post_image.putpixel((i, j), (r, g, b))
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        return

    def filter_b_w(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        for i in range(0, self.post_image.size[0] - 1):
            for j in range(0, self.post_image.size[1] - 1):
                r, g, b = self.post_image.getpixel((i, j))
                S = r + g + b
                if (S > (((255 + 1) // 2) * 3)):
                    r, g, b = 255, 255, 255
                else:
                    r, g, b = 0, 0, 0
                self.post_image.putpixel((i, j), (r, g, b))
        self.post_image.save('temps/test3.jpg')
        self.paint_image('temps/test3.jpg')
        return

    def open_file(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', "*jpg *tif *png *gif *bmp")[0]
            self.hidden_name = fname
            pixmap = QPixmap(fname)
            self.image = Image.open(fname)
            self.lineEdit.setText(f'Путь: {os.path.abspath(fname)}')
            self.paint_image(fname)
            self.open_blocks()
        except:
            print('Nein')
        return

    def save_file(self):
        self.pushButton_15.setEnabled(True)
        self.b_c_DEactivate()
        self.post_image.save(self.hidden_name)

    def save_how_file(self):
        try:
            fname_save = QFileDialog.getSaveFileName(self, 'Save File', '/home', "*jpg *tif *png *gif *bmp")[0]
            self.post_image.save(fname_save)
        except:
            print('Nein')
        return

    def paint_image(self, image, b_c=False, set_geometry=False):
        self.textEdit.setText(str(self.horizontalSlider.value()))
        self.textEdit_2.setText(str(self.horizontalSlider_2.value()))
        try:
            self.label_11.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            pixmap = QPixmap(image)
            if b_c == False:
                self.redactor_name = image
                self.post_image = Image.open(image)

            if str(type(self.post_image.getpixel((0, 0)))) == "<class 'int'>" and self.block == False:
                self.pushButton_4.setEnabled(False)
            if str(type(self.post_image.getpixel((0, 0)))) == "<class 'tuple'>" and self.block == False:
                self.pushButton_4.setEnabled(True)
            # изменение размера для того чтобы оно влезло в лейбл
            self.w = pixmap.width()
            self.h = pixmap.height()
            if pixmap.width() > self.label_11.width():
                pixmap = pixmap.scaledToWidth(self.label_11.width())
            elif pixmap.height() > self.label_11.height():
                pixmap = pixmap.scaledToHeight(self.label_11.width())
            if set_geometry == 'up':
                pixmap = pixmap.scaledToWidth(self.label_11.width() + self.koef)
                pixmap = pixmap.scaledToWidth(self.label_11.width() + self.koef)
            elif set_geometry == 'down':
                pixmap = pixmap.scaledToWidth(self.label_11.width() + self.koef)
                pixmap = pixmap.scaledToWidth(self.label_11.width() + self.koef)

            self.label_11.setPixmap(pixmap)
            # печать размера
            self.lineEdit_2.setText(f'Ширина: {self.w}')
            self.lineEdit_3.setText(f'Высота: {self.h}')

            # переводим вес в подходящую велечину
            db_chek = ['kb', 'mb', 'gb']
            db = os.path.getsize(image) / 1024
            while len(str(int(db))) > 3:
                db /= 1024
                db_chek.pop(0)
            self.lineEdit_4.setText('Размер: {:.2f} {}'.format(db, db_chek[0]))

        except:
            print('Nein')
        # try:
        #     os.remove(image)
        # except:
        #     print('file not_found')
        # return


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Photo_Editor()
    window.show()
    app.exec_()
