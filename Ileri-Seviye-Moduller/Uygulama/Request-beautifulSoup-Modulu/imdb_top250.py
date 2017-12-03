import requests
from bs4 import BeautifulSoup

url="http://www.imdb.com/chart/top" #link
response=requests.get(url) #istekte bulunduk
html_icerigi=response.content #html içeriğini aldık
soup=BeautifulSoup(html_icerigi,"html.parser") #soup ile düzenledik

a=float(input("Rating'i giriniz:"))

basliklar=soup.find_all("td",{"class":"titleColumn"}) #basliklari soup.find_all() metodu ile çektik
ratingler= soup.find_all("td",{"class":"ratingColumn imdbRating"})#ratingleri soup.find_all() metodu ile çektik

for baslik,rating in zip(basliklar,ratingler):
    baslik=baslik.text #yalnızca text içeriği kalsın html taglarından arındırdık.
    rating=rating.text #yalnızca text içeriği kalsın html taglarından arındırdık.

    baslik=baslik.strip()#bastaki ve sondaki boşluklardan arındırdık.
    baslik=baslik.replace("\n","") #\n leri kaldırdık
    baslik=baslik.replace("    ","") # 4 karakterlik boşluğu kaldırdık
    baslik=baslik[4:] #içerik 01 Film adı gibiydi baştaki 01 kaldırıldı 4.indisten başla diyerek
    rating=rating.strip()
    rating=rating.replace("\n","")
    if(float(rating)>a):
        print("Film ismi:{} --> Rating:{}".format(baslik,rating))
