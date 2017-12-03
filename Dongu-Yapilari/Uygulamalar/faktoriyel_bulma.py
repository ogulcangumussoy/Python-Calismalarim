print("""
*******************************
Faktöriyel Bulma Programı

Çıkmak için q'ya basınız.

*******************************
""")
while True:
    sayi = input("Bir sayı giriniz: ")
    if(sayi == "q"):
        print("Program sonlanıyor...")
        break
    else:
        sayi=int(sayi)
        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel*=i
            print("{} Faktoriyel".format(i), faktoriyel)
        print("Faktöriyel:",faktoriyel)
