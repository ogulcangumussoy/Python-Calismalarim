#Kwargs kullanımı: Argümanları sözlük şeklinde geri döndürür.

def fonksiyon(**kwargs):
    print(kwargs)

fonksiyon(isim="Murat",soyisim="Coşkun",numara=12345)

#Çıktı sözlük şeklinde {'soyisim':'Coşkun',.....}
