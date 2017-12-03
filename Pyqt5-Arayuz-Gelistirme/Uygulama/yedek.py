from PyQt5.QtWidgets import QApplication,QRadioButton,QLineEdit,QWidget,QMainWindow,QAction,qApp,QHBoxLayout,QVBoxLayout,QFileDialog,QPushButton,QTextEdit,QLabel
import sys
from PyQt5 import QtGui

def func(self):
    layout=QtGui.QHBoxLayout()  # layout for the central widget
    widget=QtGui.QWidget(self)  # central widget
    widget.setLayout(layout)

    number_group=QtGui.QButtonGroup(widget) # Number group
    r0=QtGui.QRadioButton("0")
    number_group.addButton(r0)
    r1=QtGui.QRadioButton("1")
    number_group.addButton(r1)
    layout.addWidget(r0)
    layout.addWidget(r1)

    letter_group=QtGui.QButtonGroup(widget) # Letter group
    ra=QtGui.QRadioButton("a")
    letter_group.addButton(ra)
    rb=QtGui.QRadioButton("b")
    letter_group.addButton(rb)
    layout.addWidget(ra)
    layout.addWidget(rb)

    # assign the widget to the main window
    self.setCentralWidget(widget)
    self.show()
app=QApplication(sys.argv)
func=func()
sys.exit(app.exec_())
