"""
Problem 1: Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın
ve şu kurallara göre ekrana şu yazıları yazdırın.

    Beden Kitle İndeksi : Kilo / Boy(m) * Boy(m)

    BKİ 18.5'in altındaysa -----------> Zayıf

    BKİ 18.5 ile 25 arasındaysa   ----------> Normal

    BKİ 25 ile 30 arasındaysa  -------> Fazla Kilolu

    BKİ 30'un üstündeyse ----------> Obez

"""

boy = int(input("Boyunuzu giriniz: "))
kilo = int(input("Kilonuzu giriniz: "))

bki = kilo/(boy/100)**2

if(bki< 18.5):
    print("Zayıf")
elif(bki >= 18.5 and bki<25):
    print("Normal")
elif(bki >= 25 and bki<30):
    print("Fazla Kilolu")
elif(bki > 30):
    print("Obez")
