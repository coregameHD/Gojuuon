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
        self.ui.a_button.clicked.connect(lambda: QSound.play("media/sound/a.wav"))
        self.ui.i_button.clicked.connect(lambda: QSound.play("media/sound/i.wav"))
        self.ui.u_button.clicked.connect(lambda: QSound.play("media/sound/u.wav"))
        self.ui.e_button.clicked.connect(lambda: QSound.play("media/sound/e.wav"))
        self.ui.o_button.clicked.connect(lambda: QSound.play("media/sound/o.wav"))

        self.ui.ka_button.clicked.connect(lambda: QSound.play("media/sound/ka.wav"))
        self.ui.ki_button.clicked.connect(lambda: QSound.play("media/sound/ki.wav"))
        self.ui.ku_button.clicked.connect(lambda: QSound.play("media/sound/ku.wav"))
        self.ui.ke_button.clicked.connect(lambda: QSound.play("media/sound/ke.wav"))
        self.ui.ko_button.clicked.connect(lambda: QSound.play("media/sound/ko.wav"))

        self.ui.sa_button.clicked.connect(lambda: QSound.play("media/sound/sa.wav"))
        self.ui.shi_button.clicked.connect(lambda: QSound.play("media/sound/shi.wav"))
        self.ui.su_button.clicked.connect(lambda: QSound.play("media/sound/su.wav"))
        self.ui.se_button.clicked.connect(lambda: QSound.play("media/sound/se.wav"))
        self.ui.so_button.clicked.connect(lambda: QSound.play("media/sound/so.wav"))

        self.ui.ta_button.clicked.connect(lambda: QSound.play("media/sound/ta.wav"))
        self.ui.chi_button.clicked.connect(lambda: QSound.play("media/sound/chi.wav"))
        self.ui.tsu_button.clicked.connect(lambda: QSound.play("media/sound/tsu.wav"))
        self.ui.te_button.clicked.connect(lambda: QSound.play("media/sound/te.wav"))
        self.ui.to_button.clicked.connect(lambda: QSound.play("media/sound/to.wav"))

        self.ui.na_button.clicked.connect(lambda: QSound.play("media/sound/na.wav"))
        self.ui.ni_button.clicked.connect(lambda: QSound.play("media/sound/ni.wav"))
        self.ui.nu_button.clicked.connect(lambda: QSound.play("media/sound/nu.wav"))
        self.ui.ne_button.clicked.connect(lambda: QSound.play("media/sound/ne.wav"))
        self.ui.no_button.clicked.connect(lambda: QSound.play("media/sound/no.wav"))

        self.ui.ha_button.clicked.connect(lambda: QSound.play("media/sound/ha.wav"))
        self.ui.hi_button.clicked.connect(lambda: QSound.play("media/sound/hi.wav"))
        self.ui.fu_button.clicked.connect(lambda: QSound.play("media/sound/fu.wav"))
        self.ui.he_button.clicked.connect(lambda: QSound.play("media/sound/he.wav"))
        self.ui.ho_button.clicked.connect(lambda: QSound.play("media/sound/ho.wav"))

        self.ui.ma_button.clicked.connect(lambda: QSound.play("media/sound/ma.wav"))
        self.ui.mi_button.clicked.connect(lambda: QSound.play("media/sound/mi.wav"))
        self.ui.mu_button.clicked.connect(lambda: QSound.play("media/sound/mu.wav"))
        self.ui.me_button.clicked.connect(lambda: QSound.play("media/sound/me.wav"))
        self.ui.mo_button.clicked.connect(lambda: QSound.play("media/sound/mo.wav"))

        self.ui.ya_button.clicked.connect(lambda: QSound.play("media/sound/ya.wav"))
        self.ui.yu_button.clicked.connect(lambda: QSound.play("media/sound/yu.wav"))
        self.ui.yo_button.clicked.connect(lambda: QSound.play("media/sound/yo.wav"))

        self.ui.ra_button.clicked.connect(lambda: QSound.play("media/sound/ra.wav"))
        self.ui.ri_button.clicked.connect(lambda: QSound.play("media/sound/ri.wav"))
        self.ui.ru_button.clicked.connect(lambda: QSound.play("media/sound/ru.wav"))
        self.ui.re_button.clicked.connect(lambda: QSound.play("media/sound/re.wav"))
        self.ui.ro_button.clicked.connect(lambda: QSound.play("media/sound/ro.wav"))

        self.ui.wa_button.clicked.connect(lambda: QSound.play("media/sound/wa.wav"))
        self.ui.wo_button.clicked.connect(lambda: QSound.play("media/sound/wo.wav"))

        self.ui.n_button.clicked.connect(lambda: QSound.play("media/sound/n.wav"))

def main():
    app = QApplication(sys.argv)
    w = Gojuuon()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
