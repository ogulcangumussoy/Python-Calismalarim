from PyQt5.QtWidgets import QApplication,QRadioButton,QLineEdit,QWidget,QMainWindow,QAction,qApp,QHBoxLayout,QVBoxLayout,QFileDialog,QPushButton,QTextEdit,QLabel
import sys,requests,sqlite3,locale
from PyQt5 import QtGui
from datetime import date,datetime

locale.setlocale(locale.LC_ALL,"")
class Menu(QMainWindow):
    pass
class Uygulama(QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()
        self.sayac=0
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("database.db")
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS gozlemler(id INTEGER PRIMARY KEY AUTOINCREMENT,tarih TEXT,mevcut_doviz TEXT,cevirilen_doviz TEXT,miktar INT,sonuc TEXT)")
        self.baglanti.commit()
    def init_ui(self):
        self.url="http://api.fixer.io/latest?base="
        self.mevcutlabel=QLabel("Mevcut Döviz(USD,TRY,EUR)")
        self.mevcutdoviz=QLineEdit()
        self.cevirilabel=QLabel("Çevirilecek Döviz(USD,TRY,EUR)")
        self.ceviridoviz=QLineEdit()
        self.miktarlabel=QLabel("Çevirilecek Miktar")
        self.miktar=QLineEdit("")
        self.sonuc=QLabel("")
        self.hesapla=QPushButton("Hesapla")
        self.kaydet=QPushButton("Veritabanına Kaydet")
        self.resim=QLabel()
        self.resim.setPixmap(QtGui.QPixmap("borsa.png"))

        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.hesapla)
        h_box.addWidget(self.kaydet)

        v_box=QVBoxLayout()
        v_box.addWidget(self.resim)
        v_box.addWidget(self.mevcutlabel)
        v_box.addWidget(self.mevcutdoviz)
        v_box.addWidget(self.cevirilabel)
        v_box.addWidget(self.ceviridoviz)
        v_box.addWidget(self.miktarlabel)
        v_box.addWidget(self.miktar)
        v_box.addWidget(self.sonuc)
        v_box.addStretch()
        v_box.addLayout(h_box)
        self.setLayout(v_box)

        self.setWindowTitle("Döviz Hesaplama -- ©DovKUR")
        self.show()

        self.hesapla.clicked.connect(self.click)
        self.kaydet.clicked.connect(self.click)

    def click(self):
        sender=self.sender()

        if sender.text() == "Hesapla":
            self.birinci_doviz=self.mevcutdoviz.text()
            self.ikinci_doviz=self.ceviridoviz.text()
            self.miktar2=int(self.miktar.text())

            response = requests.get(self.url+self.birinci_doviz)
            json_verisi=response.json()
            try:
                sonuc=float(json_verisi["rates"][self.ikinci_doviz]*self.miktar2)
                self.sonuc.setText("Hesaplama sonucu: "+str(sonuc)+self.ikinci_doviz)
                self.sayac=1
            except KeyError:
                self.sayac=0
                self.sonuc.setText("Lütfen para birimini doğru giriniz.")
        elif sender.text() == "Veritabanına Kaydet":
                su_an=datetime.now()
                su_an=str(datetime.strftime(su_an,"%X"))
                if(self.sayac == 1):
                    self.cursor.execute("INSERT INTO gozlemler(tarih,mevcut_doviz,cevirilen_doviz,miktar,sonuc) VALUES(?,?,?,?,?)",(su_an,self.mevcutdoviz.text(),self.ceviridoviz.text(),self.miktar.text(),self.sonuc.text()))
                    self.baglanti.commit()
                    self.sonuc.setText("Kayıt Başarılı")
                    self.sayac=0
                else:
                    self.sonuc.setText("Kayıt Başarısız öncelikle sonucu hesaplayın.")


app= QApplication(sys.argv)
uygulama=Uygulama()
sys.exit(app.exec_())
