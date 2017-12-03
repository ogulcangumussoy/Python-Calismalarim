import sqlite3
import time

class Sarki():

    def __init__(self,isim,sanatci,album,produksiyon_sirketi,sure):
        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.produksiyon_sirketi = produksiyon_sirketi
        self.sure = sure
    def __str__(self):
        return "Şarkı İsmi:{}\nSanatçı:{}\nAlbüm:{}\nProdüksiyon Şirketi:{}\nSüre:{}".format(self.isim,self.sanatci,self.album,self.produksiyon_sirketi,self.sure)

class Metodlar():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("muzik_projesi.db")
        self.cursor=self.baglanti.cursor()

        sorgu="CREATE TABLE IF NOT EXISTS sarkilar(isim TEXT, sanatci TEXT,album TEXT,produksiyon_sirketi TEXT,sure INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def sarkilari_goster(self):

        sorgu="SELECT * FROM sarkilar"

        self.cursor.execute(sorgu)

        sarkilar= self.cursor.fetchall()

        if(len(sarkilar) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4]) #döngüde buket içinden verileri alıp nesnemize yükledik
                print(sarki) # __str__ fonksiyonuna gider.
    def baglantiyi_kes(self):
        self.baglanti.close()
    def toplam_sure_hesapla(self):
        sorgu = "SELECT SUM(sure) FROM sarkilar"
        self.cursor.execute(sorgu)
        sure = self.cursor.fetchall()
        return sure[0][0]
    def sarki_ekle(self,sarki):
        sorgu = "INSERT INTO sarkilar VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.produksiyon_sirketi,sarki.sure))
        self.baglanti.commit()
    def sarki_sil(self,isim):
        sorgu = "DELETE FROM sarkilar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
