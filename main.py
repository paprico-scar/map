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
        self.butt.clicked.connect(self.show_map)

    def show_map(self):
        ll = ['ll', self.coord_x.text() + ',' + self.coord_y.text()]
        spn = ['spn', self.spn.text()]
        my_map = zapros(ll, spn)
        im = Image.open(BytesIO(my_map.content))
        im.save('map.png')
        pixmap = QPixmap('map.png')
        self.map.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec_())
