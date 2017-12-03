from PyQt5 import QtWidgets
import sys

def Pencere():

    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Ders3 Buton Oluşturma")
    label=QtWidgets.QLabel(pencere)
    label.setText("Ders 3'de Buton oluşturduk")
    label.move(150,10)
    buton=QtWidgets.QPushButton(pencere)
    buton.setText("Gönder")
    buton.move(150,30)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()
