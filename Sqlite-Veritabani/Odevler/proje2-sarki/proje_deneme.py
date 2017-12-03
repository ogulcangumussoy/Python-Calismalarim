from sarki import *

print("""
*********************************
Müzik Programı'na Hoşgelniz....

İşlemler:
1)Şarkıları Göster
2)Toplam şarkı süresi
3)Şarkı Ekle
4)Şarkı Sil

Çıkmak için 'q'ya basınız.
*********************************
""")
metodlar = Metodlar()

while True:
    islem= input("Yapılacak işlemi seçiniz: ")
    if(islem == "q"):
        print("Programdan çıkılıyor...")
        time.sleep(1)
        print("Yine bekleriz...")
    elif(islem == "1"):
        metodlar.sarkilari_goster()
    elif(islem == "2"):
        sonuc= metodlar.toplam_sure_hesapla()
        print(sonuc)
    elif(islem == "3"):
        isim = input("İsim: ")
        sanatci = input("Sanatçı: ")
        album = input("Albüm :")
        produksiyon_sirketi = input("Prodüksiyon Şirketi: ")
        sure = input("Süre: ")
        yeni_sarki = Sarki(isim,sanatci,album,produksiyon_sirketi,sure) # __ init __ metoduna attık
        print("Şarkı Ekleniyor")
        time.sleep(2)
        metodlar.sarki_ekle(yeni_sarki)
        print("Şarkı Eklendi..")
    elif(islem == "4"):
        isim = input("Silinecek şarkı ismi:")
        onay = input("Emin misiniz? [E,H]")
        if(onay == "E"):
            metodlar.sarki_sil(isim)
