import sqlite3 #kütüphaneyi dahil ettik
#veritabanı bağlantısını kurduk.
con= sqlite3.connect("kutuphane.db")
cursor=con.cursor() #bağlantı üzerinde imleç oluşturduk bu artık cursorda ve tüm işlemlerimizi burda yapıcaz.
con.close()
