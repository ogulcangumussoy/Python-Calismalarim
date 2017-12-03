"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulun.
sayının rakamlarının dördüncü üslerin toplamı o sayıya eşitse

1^4 + 2^4 + 3^4 == 123 ?
"""
print("""
******************
ARMSTRONG SAYISI BULMA PROGRAMI (Çıkmak için 'q'ya basınız.)
******************
""")

while True:
    alinan_sayi= input("Sayi giriniz: ")
    if(alinan_sayi == "q"):
        print("Programdan Çıkılıyor.")
        break
    else:
        alinan_sayi=int(alinan_sayi)
        basamak = 0
        toplam=0
        gecici_sayi= alinan_sayi

        while(gecici_sayi > 0):
            basamak = gecici_sayi %10
            toplam+=basamak**4
            gecici_sayi //=10
        if(toplam==alinan_sayi):
            print("{} sayisi Armstrong sayisidir".format(alinan_sayi))
            continue
        else:
            print("{} sayisi Armstrong sayisi değildir.".format(alinan_sayi))
            continue
