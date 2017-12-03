import sqlite3

con=sqlite3.connect("veritabani/kutuphane.db")

cursor=con.cursor() #cursor oluşturduk.

def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    liste=cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri..")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("SELECT isim,yazar,sayfa_sayisi FROM kitaplik") #küçük harf girdim kabul etti.
    liste=cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri")
    for i in liste:
        print(i)
def sartli_veri_al(yayinevi):
    cursor.execute("SELECT * FROM kitaplik WHERE yayinevi = ?",(yayinevi,))
    liste=cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri")
    for i in liste:
        print(i)
sartli_veri_al("Everest")
con.close()
