"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

"""

a=int(input("Sayi 1: "))
b=int(input("Sayi 2: "))
c=int(input("Sayi 3: "))

if(a>b and a>c):
    print("En büyük Sayi 1")
elif(b>a and b>c):
    print("En büyük Sayi 2")
elif(c>a and c>b):
    print("En büyük Sayi 3")
else:
    print("En büyük sayı yok veya tekil değil")
