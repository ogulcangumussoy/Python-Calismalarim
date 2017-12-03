"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgen mi yoksa dörtgen mi
tipini öğrenebilmek için soru sorun.

Eğer dörtgen ise 4 üçgen ise 3 kenarının uzunluğunu alın.
Dörtgense kare veya dikdörtgen
Üçgense eşkenar ikizkenar çeşitkenar mı yada üçgen değil mi
Mutlak değer kullanın(abs)
"""
sekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz?")

if(sekil == "Dörtgen"):
    print("Lütfen kenarları sırasıyla giriniz. ")
    a=int(input("Kenar-1:"))
    b=int(input("Kenar-2:"))
    c=int(input("Kenar-3:"))
    d=int(input("Kenar-4:"))

    if(a==b and a==c and a==d):
        print("Kare")
    elif(a==c and b==d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")

elif(sekil == "Üçgen"):
    print("Lütfen kenarları sırasıyla giriniz. ")
    a=int(input("Kenar-1:"))
    b=int(input("Kenar-2:"))
    c=int(input("Kenar-3:"))
    if(abs(a+b) >c and abs(a+c) > b and abs(b+c) > a ):
        if(a==b and a==c):
            print("Eşkenar Üçgen")
        elif((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")

    else:
        print("Üçgen belirtmiyor")

else:
    print("Geçersiz Şekil")
