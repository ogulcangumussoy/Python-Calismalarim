"""
Linux için pyqt5 kurulumu
    1.Terminal aç
    2."sudo apt-get install python3-pyqt5"
    3."sudo apt-get insall python3-pyqt5.qtsql"
    4."sudo apt-get install qttools5-dev-tools"
"""
from PyQt5 import QtWidgets
import sys

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 1")
    pencere.show()

    sys.exit(app.exec_())

Pencere()
