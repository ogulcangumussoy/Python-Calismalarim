"""
Horizantal:yatay
Vertical:Dikey olarak yerleştirme yapacağız.

Örnek QHBOXLayout() için yapıldı QVBOXLayour() ise dikeyde yerleştirme yapar

"""

from PyQt5 import QtWidgets
import sys

def Pencere():

    app=QtWidgets.QApplication(sys.argv)
    okey=QtWidgets.QPushButton("Tamam") #Buton metni "Tamam"
    cencel = QtWidgets.QPushButton("İptal")
    h_box= QtWidgets.QHBoxLayout()#Dikey layoutu oluşturduk
    h_box.addStretch() #Eğer boşluğu burda bırakırsak okey ve cencel sağa yapışık olur aksi takdirde sola
    h_box.addWidget(okey) #butonları layout içerisine yerleştirdik
    #h_box.addStretch() #ortalarına koyarsak ikisinide iki tarafa sabitler ortası boşluk olur
    h_box.addWidget(cencel)
    #h_box.addStretch()#Normal şartlarda Horizantal da tüm genişliği butonlar kaplar. Stretch ile sadece
                    # butonlar kendi alanlarını kaplıyor ve pencere büyütülünce konumları sabit kalıyor.

    v_box=QtWidgets.QVBoxLayout() #Dikey layout oluştu
    v_box.addStretch() #Yukardan boşluk oluşturduk
    v_box.addLayout(h_box)

    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Ders4 Horizantal ve Vertical Box Layout Olusturma")

    pencere.setLayout(v_box)

    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()
