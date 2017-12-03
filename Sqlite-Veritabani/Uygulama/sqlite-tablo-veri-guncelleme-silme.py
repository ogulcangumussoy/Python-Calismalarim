import sqlite3
import time

con=sqlite3.connect("veritabani/kutuphane.db")
cursor=con.cursor()

def verileri_guncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("UPDATE kitaplik SET Yayinevi = ? WHERE Yayinevi = ?",(yeni_yayinevi,eski_yayinevi))
    con.commit() #veri tabanı güncelleme yaptığımız için commit ettik.
def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    liste=cursor.fetchall()
    for i in liste:
        print(i)
def verileri_sil(yazar):
    cursor.execute("DELETE FROM kitaplik WHERE Yazar = ?",(yazar,))
    con.commit()
verileri_al()

while True:
    print("""
*****************************
KÜTÜPHANE OTOMASYONU
*****************************
Seçenekler:
1)Verileri Getir
2)Verileri Güncelle
3)Verileri Sil
4)Programdan Çıkış

""")
    secenek = int(input("Seçiminiz:"))
    if(secenek == 1):
        verileri_al()
    elif(secenek == 2):
        eski_yayinevi=input("Eski Yayınevi:")
        yeni_yayinevi=input("Yeni Yayınevi:")
        verileri_guncelle(eski_yayinevi,yeni_yayinevi)
    elif(secenek==3):
        yazar=input("Silinecek yazar:")
        verileri_sil(yazar)
    elif(secenek==4):
        print("Programdan çıkılıyor..")
        time.sleep(2)
        break
con.close()
