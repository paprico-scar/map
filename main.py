from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys


class Map(QMainWindow):
    def __init__(self):
        super(Map, self).__init__()
        self.api_start = 'https://geocode-maps.yandex.ru/1.x'

    def initUI(self):
        uic.loadUi('widget.ui', self)
        self.butt.clicked.connect(self.shoe_map)

    def show_map(self):
        coords = self.coord_x.text() + ',' + self.coord_y.text()
        spn = self.spn.text()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec_())
