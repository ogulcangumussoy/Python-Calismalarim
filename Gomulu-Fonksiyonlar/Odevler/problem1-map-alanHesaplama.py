"""
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olunsun.
    [(3,4),(10,3),(5,6),(1,9)]
Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına
şöyle bir liste yazıdırın.
[12,30,30,9]
Not: map() fonksiyonunu kullanın.
"""

def alanBul(demet):
    return demet[0]*demet[1]

liste=[(3,4),(10,3),(5,6),(1,9)]

print(list(map(alanBul,liste)))

