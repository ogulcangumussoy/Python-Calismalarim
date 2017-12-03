from PyQt5 import QtWidgets,QtGui
import sys
def Pencere():
    app = QtWidgets.QApplication(sys.argv)#Uygulama oluşturduk
    pencere=QtWidgets.QWidget()#pencere oluşturduk
    pencere.setWindowTitle("PyQt5 Ders 2") #başlık bilgisini girdik
    etiket1=QtWidgets.QLabel(pencere) #Label oluşturduk ve pencereye yerleştirdik
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("Python.png"))
    etiket1.setText("Bu bir yazıdır.") #Label metnini değiştirdik
    etiket1.move(200,230) #Konumu başlangıçtan 200 sağ 30 aşağı
    etiket2.move(75,0)
    pencere.setGeometry(100,100,500,500)#100,100'den başla soldan boyut 500 500
    pencere.show() #pencreyi gösterdik

    sys.exit(app.exec_()) #ç
Pencere()
