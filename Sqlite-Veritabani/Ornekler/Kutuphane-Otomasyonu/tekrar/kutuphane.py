import sqlite3
import time

class Kitap():
    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return "Kitap İsmi:{}\nYazar:{}\nYayınevi:{}\nTur:{}\nBaskı:{}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)

class Kutuphane():
    def __init__(self):
        self.baglanti_olustur() #Kütüphane nesnesi oluşturunca otomatikman bağlantı oluşturacak.

    def baglanti_olustur(self):
        self.baglanti= sqlite3.connect("kutuphane.db") #Veritabanı oluştu
        self.cursor=self.baglanti.cursor() #Cursor Oluştu

        sorgu ="CREATE TABLE IF NOT EXISTS kitaplar(İsim TEXT,yazar TEXT,yayinevi TEXT,tur TEXT,baski INT)"

        self.baglanti.execute(sorgu) #sorguyu çalıştırdık
        self.baglanti.commit()#bağlantıyı veritabanına yönlendirdik tanıttık..
    def baglantiyi_kes(self):
        self.baglanti.close()
    def kitaplari_goster(self):

        sorgu = "SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall() #tüm verileri kitaplar listesine attık.

        if(len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4]) #döngüde buket içinden verileri  alıp nesnemize yükledik.
                print(kitap) # __str__ fonksiyonuna gider
    def kitaplari_sorgula(self,isim):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar =self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor..")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0][0],i[0][1],i[0][2],i[0][3],i[0][4])
                print(kitap)
    def kitap_ekle(self,kitap):
        sorgu = "INSERT INTO kitaplar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit()
    def kitap_sil(self,isim):
        sorgu= "DELETE FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def baski_yukselt(self,isim):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            baski = kitaplar[0][4] #kitaplarin 4.indis sütunu baski ya eriştik
            baski +=1
            sorgu2 = "UPDATE kitaplar SET baski = ? WHERE isim = ?"
            self.cursor.execute(sorgu2,(baski,isim))
            self.baglanti.commit()
