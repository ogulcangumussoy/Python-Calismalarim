"""
Değer döndürme için return kullanılır.
"""

def toplama(a,b,c):
    return a+b+c

def ikiylecarp(a):
    return a*2
toplam= toplama(3,4,5)
print(ikiylecarp(toplam))

def uclecarp(a):
    print("1.fonksiyon çalıştı...")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı...")
    return a+2
def dordebol(a):
    print("3.fonksiyon çalıştı")
    return a/4

print(dordebol(ikiyletopla(uclecarp(5))))
