"""
Bir değişken fonksiyonda tanımlanmışsa yereldir. Ve işlem bitince bellekten silinir. Başka yerden erişilemez.

Global değişkenler tanımlandığı durumlarda programın her yerinden ulaşılabilir.
"""

def fonksiyon():
    a=10
    print(a)

fonksiyon()
#print(a) //bu sekilde tanımlanmaz yerel değişkene ulaşım yok.

b=5 #global tanımladık.

def fonksiyon2():
    print(b) #"b" global olduğu için her yerden çekilir.
fonksiyon2()

#***************************
d=10
def fonksiyon3():
    global d #global e erişip orayı 25 yaptık
    d=25
    print(d)
fonksiyon3() #ikiside 25 basar
print(d)
#****************************
if True: #if blokları içerisindeki değerler global sayılır.
    e=4
    print(e)
print(e)
