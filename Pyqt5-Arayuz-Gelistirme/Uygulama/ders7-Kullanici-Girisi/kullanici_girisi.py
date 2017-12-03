import sys
from PyQt5 import QtWidgets
import sqlite3

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()
    def baglanti_olustur(self):
        baglanti=sqlite3.connect("database.db")
        self.cursor=baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler(kullanici_adi TEXT,parola TEXT)")
        baglanti.commit() #tablo güncelledik

    def init_ui(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)#Parolayı gizleme işi
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani= QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.show()

    def login(self):
        adi=self.kullanici_adi.text()
        par=self.parola.text()

        self.cursor.execute("SELECT * FROM uyeler WHERE kullanici_adi=? AND parola= ?",(adi,par))
        data=self.cursor.fetchall() #tüm verileri liste şeklinde aldık
        if(len(data) == 0):
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoşgeldiniz "+adi)
app = QtWidgets.QApplication(sys.argv)
pencere= Pencere()
sys.exit(app.exec_()) #Programın açık kalması için gerekli
