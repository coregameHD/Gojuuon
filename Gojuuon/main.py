import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from gojuuon_ui import Ui_Form

class Gojuuon(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Image Banner
        self.img_label = QLabel(self)
        self.imgPath = QPixmap("media/img/gojuuon-banner-new.jpg")
        self.img_label.setPixmap(self.imgPath)

def main():
    app = QApplication(sys.argv)
    w = Gojuuon()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
