"""
Mantık olarak list comprehension'a benzer.
liste1=[1,2,3,4,5]

liste2=[i*2 for i in liste1] ile liste2'ye değerleri attık.

"""

def ikiylecarp(x):
    return x*2

print(ikiylecarp(3))

#bunun yerine lambda kullanılabilir.

ikiylecarp2 = lambda x : x*2 #x girip x*2 return etsin
print(ikiylecarp2(5))

toplama= lambda x,y,z: x+y+z
print(toplama(2,4,6))

terscevir= lambda s: s[::-1] #sayıyı ters çevirir.
print(terscevir("ahmet"))

sayiciftmi= lambda s: s%2==0 #sayı çift mi kontrol eder.
print(sayiciftmi(6))
