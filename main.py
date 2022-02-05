from io import BytesIO
from PIL import Image
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
import sys


def zapros(*args):
    param = {'l': 'map',
             'size': '450,450'}
    map_api_server = 'https://static-maps.yandex.ru/1.x/'
    for i in args:
        if i[1] == '':
            continue
        param[i[0]] = i[1]
    request = requests.get(map_api_server, params=param)
    return request


class Map(QMainWindow):
    def __init__(self):
        super(Map, self).__init__()
        uic.loadUi('widget.ui', self)
        self.spnn = ''
        self.lll = ''
        self.butt.clicked.connect(self.first_show_map)
        self.up.clicked.connect(self.do_up)
        self.down.clicked.connect(self.do_down)

    def first_show_map(self):
        self.spnn = ['spn', self.spn.text()]
        self.lll = ['ll', self.coord_x.text() + ',' + self.coord_y.text()]
        if self.spnn[1] == '':
            self.spnn = ['spn', '1,1']
        my_map = zapros(self.lll, self.spnn)
        im = Image.open(BytesIO(my_map.content))
        im.save('map.png')
        pixmap = QPixmap('map.png')
        self.map.setPixmap(pixmap)

    def show_map(self):
        if self.spnn[1] == '':
            self.spnn = ['spn', '1,1']
        my_map = zapros(self.lll, self.spnn)
        im = Image.open(BytesIO(my_map.content))
        im.save('map.png')
        pixmap = QPixmap('map.png')
        self.map.setPixmap(pixmap)

    def do_up(self):
        new_spnn = [float(i) for i in self.spnn[1].split(',')]
        if new_spnn[1] - 0.05 > 0:
            new_spnn = [str(i - 0.05) for i in new_spnn]
            new_spnn = ','.join(new_spnn)
            self.spnn = ['spn', new_spnn]
        self.show_map()

    def do_down(self):
        new_spnn = [float(i) for i in self.spnn[1].split(',')]
        if new_spnn[1] + 0.05 > 0:
            new_spnn = [str(i + 0.05) for i in new_spnn]
            new_spnn = ','.join(new_spnn)
            self.spnn = ['spn', new_spnn]
        self.show_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec_())
