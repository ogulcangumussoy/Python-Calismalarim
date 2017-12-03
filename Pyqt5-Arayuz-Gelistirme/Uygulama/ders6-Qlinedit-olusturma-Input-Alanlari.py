import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani=QtWidgets.QLineEdit() #Yazı yazabileceğimiz alan
        self.temizle=QtWidgets.QPushButton("Temizle")
        self.yazdir=QtWidgets.QPushButton("Yazdır")
        self.sonuc=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)
        v_box.addWidget(self.sonuc)
        v_box.addStretch()

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)

        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)

        self.show()

    def click(self):
        sender=self.sender() #QtWidgets içerisinde sender fonksiyonu var bu butonun textini alıyor
                             # bu değere göre işlem yapacağız.
        if sender.text() == "Temizle":
            self.yazi_alani.clear() #yazı alanını clear metodu ile temizler
        else:
            self.sonuc.setText(self.yazi_alani.text()) #yazılan metni terminale basar
#uygulama başlat
app=QtWidgets.QApplication(sys.argv)
pencere= Pencere()
sys.exit(app.exec_())
