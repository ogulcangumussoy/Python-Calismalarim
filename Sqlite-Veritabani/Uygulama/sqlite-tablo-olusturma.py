import sqlite3

con=sqlite3.connect("veritabani/kutuphane.db")

cursor= con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit() #sorgunun işlem yapabilmesi için gerekli


tablo_olustur()
con.close()
