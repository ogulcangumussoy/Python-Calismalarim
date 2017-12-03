import metodlar as metod
import time

print("""
********************
CALCULATOR By_GumussoySoftware (Çıkmak için 'q'ya basınız..)
********************

Fonksiyonlar:

1:Toplama
2:Çıkarma
3.Çarpma
4.Bölme
5.Karekök Alma
6.Faktoriyel Alma
""")

while True:
    islem= input("Yapılacak işlemi seçiniz: ")
    if(islem=='q'):
        print("Programdan çıkılıyor")
        metod.time.sleep(1)
        break
    else:
        islem=int(islem)
        if(islem==1):
            sayi1=int(input("Birinci sayiyi giriniz: "))
            sayi2=int(input("İkinci sayiyi giriniz: "))
            sonuc=metod.topla(sayi1,sayi2)
            print("{} + {} = {}".format(sayi1,sayi2,sonuc))
            continue
        elif(islem==2):
            sayi1=int(input("Birinci sayiyi giriniz: "))
            sayi2=int(input("İkinci sayiyi giriniz: "))
            sonuc=metod.cikart(sayi1,sayi2)
            print("{} - {} = {}".format(sayi1,sayi2,sonuc))
            continue
        elif(islem==3):
            sayi1=int(input("Birinci sayiyi giriniz: "))
            sayi2=int(input("İkinci sayiyi giriniz: "))
            sonuc=metod.carp(sayi1,sayi2)
            print("{} * {} = {}".format(sayi1,sayi2,sonuc))
            continue
        elif(islem==4):
            sayi1=int(input("Birinci sayiyi giriniz: "))
            sayi2=int(input("İkinci sayiyi giriniz: "))
            sonuc=metod.bol(sayi1,sayi2)
            print("{} / {} = {}".format(sayi1,sayi2,sonuc))
            continue
        elif(islem==5):
            sayi=int(input("Karakökü alınacak sayiyi giriniz: "))
            sonuc=metod.karekok(sayi)
            print("{} sayisinin karekökü = {}".format(sayi,sonuc))
            continue
        elif(islem==6):
            sayi=int(input("Faktöriyeli hesaplanacak sayiyi giriniz: "))
            sonuc=metod.faktoriyel(sayi)
            print("{}! = {}".format(sayi,sonuc))
            continue
        else:
            time.sleep(1)
            print("Lütfen geçerli bir işlem seçiniz...")
            continue
