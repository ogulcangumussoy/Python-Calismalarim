# def toplama(a,b,c):
#     print(a+b+c)
#
# toplama(3,4,5) #Burada 4 değer girersek hata verir. Esnek saylar buna çözüm sunar.
#
# def toplama(*a):
#     print(a)
# toplama(1,2,3,4,5,6)

def toplama(*a):
    toplam=0
    for i in a:
        toplam+=i
    print(toplam)
toplama(5,6,7,8,9,1,10)
