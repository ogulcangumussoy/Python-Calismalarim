"""
Sayı bölenlerini topladığımız zaman kendisine eşitse mükemmel sayıdır.
"""

def mukemmelSayi(sayi):
    toplam=0
    for i in range(1,sayi):
        if(sayi % i==0):
            toplam+=i
    return toplam==sayi

for i in range(1,1000):
    if(mukemmelSayi(i)):
        print(i,"Mükemmel sayıdır.")
