#mark directory as sources root seçersek from kutuphane dediğimiz zaman sorun çıkarmaz.
from kutuphane import *  # kutuphane içerisindeki herşeye erişebiliriz artık.


print("""
*****************************************
Kütüphane Programına Hoşgeldiniz.

İşlemler;

1.Kitapları Göster
2.Kitap Sorgulama
3.Kitap Ekle
4.Kitap Sil
5.Baskı Yükselt

Çıkmak için 'q'ya basınız.
*****************************************
""")

kutuphane = Kutuphane()  #bir nesne oluşturduk.

while True:
    islem = input("Yapacağınız İşlem:")
    if(islem == "q"):
        print("Programdan çıkılıyor...")
        time.sleep(1)
        print("Yine bekleriz...")
        break
    elif(islem == "1"):
        kutuphane.kitaplari_goster()

    elif(islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz ?")
        print("Kitap sorgulanıyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)
    elif(islem == "3"):
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        tur= input("Tür: ")
        baski= int(input("Baskı :"))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)

        print("Kitap Ekleniyor...")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi...")
    elif(islem=="4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?")
        cevap= input("Emin misiniz ? (E/H)")
        if(cevap == "E"):
            print("Kitap Siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap Silindi...")

    elif(islem == "5"):
        isim = input("Hangi kitabın baskını yükseltmek istiyorsunuz ?")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baskı yükseltildi...")
    else:
        print("Geçersiz İşlem...")
