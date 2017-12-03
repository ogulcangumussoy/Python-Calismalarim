import random
import time

print("""
******************
SAYI TAHMİN OYUNU
******************

1 ile 40 arasında sayıyı tahmin ediniz.

**************************
""")

rasgele_sayi=random.randint(1,40) #1 ile 40 arasında sayı üret ikiside dahil
tahmin_hakki= 7

while True:

    tahmin= int(input("Tahmininiz: "))

    if(tahmin< rasgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin")

        tahmin_hakki-=1
    elif(tahmin> rasgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin")

        tahmin_hakki-=1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Sayınız:",rasgele_sayi)
        break
    if(tahmin_hakki == 0):
        print("Tahmin hakkınız bitti...")
        print("Saynınız: ",rasgele_sayi)
        break
