import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget): #miras aldı
    def __init__(self):
        super().__init__() #pencereyi burda aldık

        self.init_ui() #ekleyeceğiz elemanları bu fonksiyonda yazacağız.
    def init_ui(self):
        self.yazi_alani=QtWidgets.QLabel("Bana Henüz Tıklanmadı..")
        self.buton=QtWidgets.QPushButton("Bana Tıkla")
        self.say=0


        v_box= QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)

        self.buton.clicked.connect(self.click) #tıkladığımız zaman click metodu çalışacak.
        self.show()
    def click(self):
        self.say+=1
        self.yazi_alani.setText("Bana {} kere Tıklandı.".format(str(self.say)))


#Görebilmek için bir uygulama oluşturmalıyız.
app= QtWidgets.QApplication(sys.argv)
pencere= Pencere() #pencere oluşturuldu
sys.exit(app.exec_())
