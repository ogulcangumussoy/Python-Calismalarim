from PyQt5.QtWidgets import *
import sys,requests
from bs4 import BeautifulSoup
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        url="http://www.imdb.com/chart/top" #link
        response=requests.get(url) #istekte bulunduk
        html_icerigi=response.content #html içeriğini aldık
        soup=BeautifulSoup(html_icerigi,"html.parser") #soup ile düzenledik

        basliklar=soup.find_all("td",{"class":"titleColumn"}) #basliklari soup.find_all() metodu ile çektik
        ratingler= soup.find_all("td",{"class":"ratingColumn imdbRating"})#ratingleri soup.find_all() metodu ile çektik

        self.layout = QVBoxLayout(self)
        self.listwidget = QListWidget(self)
        veri = QListWidgetItem("{:<120}{:<20}".format("Film Adı","Rating"), self.listwidget)
        sayac=0
        for baslik,rating in zip(basliklar,ratingler):
            sayac+=1
            baslik=baslik.text
            rating=rating.text
            baslik=baslik.strip()
            baslik=baslik.replace("\n","")
            baslik=baslik.replace("    ","")
            fark=80-len(baslik)
            baslik+=" "*fark
            rating=rating.strip()
            rating=rating.replace("\n","")
            self.listwidget.insertItem(sayac,"{}{:<20}".format(baslik,rating))

        self.buton = QPushButton("Tamam",self)
        self.layout.addWidget(self.listwidget)
        self.layout.addWidget(self.buton)
        self.setGeometry(500,0,650,750)
        self.show()

uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())
