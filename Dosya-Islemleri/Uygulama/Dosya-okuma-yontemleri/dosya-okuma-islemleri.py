"""Dosyanın olmama durumu olabilir bu durum hataya yol açacağı için
    bunu önlemek için try-except kullanabiliriz."""
try:
    file=open("Bilgiler2.txt","r") #okuma kipi(r) ile açıldı.
except FileNotFoundError:
    print("Dosya Bulunamadı...")

