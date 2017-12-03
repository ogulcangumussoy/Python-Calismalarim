import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar=self.menuBar() #menubarı oluşturduk
        dosya=menubar.addMenu("Dosya") #Menubar' dosya adında bir menü ekledik
        duzenle=menubar.addMenu("Düzenle")

        dosya_ac=QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet=QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        cikis=QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        ara_ve_degistir=duzenle.addMenu("Ara ve Değiştir.")
        ara=QAction("Ara",self)
        degistir=QAction("Değiştir",self)

        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)

        cikis.triggered.connect(self.cikis_yap)
        dosya.triggered.connect(self.response)
        self.setWindowTitle("Menüler")
        self.show()

    def cikis_yap(self):
        qApp.quit()
    def response(self,action): #python kendisi action ekliyor
        if(action.text()) == "Dosya Aç":
            print("Dosya Aç'a Basıldı")
        elif action.text() == "Dosya Kaydet":
            print("Dosya Kaydet'e Basıldı")
        elif action.text()=="Çıkış":
            print("Çıkış'a basıldı")

app =QApplication(sys.argv)
menu= Menu()
sys.exit(app.exec_())
