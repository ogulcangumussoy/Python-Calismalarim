"""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon eğer çift ise return ile bu değeri dönsün
Ancak sayı tek ise fonksiyon raise ile valueError hatası fırlatsın. Daha sonra,içinde çift ve tek sayıların bulunduğu
bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""

def sayiCiftmi(sayi):
    if(sayi % 2 ==0):
        return sayi
    else:
        raise ValueError #try except kullanırsak bunu yazdıramayız.

liste = [34,4,5,7,13,45,32,18,22,78,65,43]
for eleman in liste:
    try:
        print(sayiCiftmi(eleman))
        print(eleman)
    except ValueError:
        pass
