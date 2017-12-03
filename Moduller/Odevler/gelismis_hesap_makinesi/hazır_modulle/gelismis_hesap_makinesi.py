import math
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
    islem= input("İşlemi seçiniz:")

    if(islem=='q'):
        print("Programdan çıkış yapılıyor...")
        time.sleep(1)
        break
    else:
        islem=int(islem)
        if(islem==1):
            sayi1= int(input("Birinci sayiyi giriniz: "))
            sayi2= int(input("İkinci sayiyi giriniz: "))
            print("Sonuç hesaplanıyor....")
            time.sleep(0.5)
            print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))
            continue
        elif(islem==2):
            sayi1= int(input("Birinci sayiyi giriniz: "))
            sayi2= int(input("İkinci sayiyi giriniz: "))
            print("Sonuç hesaplanıyor....")
            time.sleep(0.5)
            print("{} - {} = {}".format(sayi1,sayi2,sayi1-sayi2))
            continue
        elif(islem==3):
            sayi1= int(input("Birinci sayiyi giriniz: "))
            sayi2= int(input("İkinci sayiyi giriniz: "))
            print("Sonuç hesaplanıyor....")
            time.sleep(0.5)
            print("{} * {} = {}".format(sayi1,sayi2,sayi1*sayi2))
            continue
        elif(islem==4):
            sayi1= int(input("Birinci sayiyi giriniz: "))
            sayi2= int(input("İkinci sayiyi giriniz: "))
            print("Sonuç hesaplanıyor....")
            time.sleep(0.5)
            print("{} / {} = {}".format(sayi1,sayi2,sayi1/sayi2))
            continue
        elif(islem==5):
            sayi= int(input("Sayiyi giriniz: "))
            print("Sonuç hesaplanıyor....")
            time.sleep(0.5)
            print("{} sayisinin karekökü = {}".format(sayi,math.sqrt(sayi)))
            continue
        elif(islem==6):
            sayi= int(input("Sayiyi giriniz: "))
            print("Sonuç hesaplanıyor....")
            time.sleep(0.5)
            print("{} sayisinin faktöriyeli = {}".format(sayi,math.factorial(sayi)))
            continue




