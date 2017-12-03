"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölünenlerinin toplamı kendine eşit ise bu sayıya "mükemmel sayı" denir. 6(1+2+3=6)
"""
print("""
*****************
Mükemmel Sayı Bulma Programı(Çıkmak için "q" ya basınız)
*****************
""")
while True:
    alinan_sayi= input("Sayıyı Giriniz: ")
    if(alinan_sayi == "q"):
        print("Çıkılıyor...")
        break
    else:
        alinan_sayi = (int(alinan_sayi))
        toplam=0
        for i in range(1,alinan_sayi):
            if(alinan_sayi%i==0):
                toplam+=i
        if(toplam==alinan_sayi):
            print("{} sayisi mükemmel sayıdır.".format(alinan_sayi))
            continue
        else:
            print("{} sayisi mükemmel sayı değildir.".format(alinan_sayi))
            continue
