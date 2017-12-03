import sqlite3

con= sqlite3.connect("veritabani/kutuphane.db")
cursor=con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Kitaplik_ID INTEGER PRIMARY KEY AUTOINCREMENT,Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("INSERT INTO kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit() #veritabanını güncelledik.
def kullanici_veri_ekle(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik Values(NULL,?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
isim= input("İsim:")
yazar = input("Yazar:")
yayinevi=input("Yayınevi:")
sayfa_sayisi= int(input("Sayfa Sayısı:"))
tablo_olustur()
kullanici_veri_ekle(isim,yazar,yayinevi,sayfa_sayisi)
con.close()
