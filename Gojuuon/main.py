import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QSound
from gojuuon_ui import Ui_Form

class Gojuuon(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Image Banner
        self.imgPath = QPixmap("media/img/gojuuon-banner-new.jpg")
        self.ui.img_banner.setPixmap(self.imgPath)
        
        # Buttons
        self.ui.a_button.clicked.connect(self.play)

    def play(self):
        QSound.play("media/sound/a.wav")

def main():
    app = QApplication(sys.argv)
    w = Gojuuon()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
