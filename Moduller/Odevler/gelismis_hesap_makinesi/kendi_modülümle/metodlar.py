import time
def topla(a,b):
    print("Sonuç hesaplanıyor...")
    time.sleep(1)
    return a+b

def cikart(a,b):
    print("Sonuç hesaplanıyor...")
    time.sleep(1)
    return a-b

def carp(a,b):
    print("Sonuç hesaplanıyor...")
    time.sleep(1)
    return a*b

def bol(a,b):
    print("Sonuç hesaplanıyor...")
    time.sleep(1)
    return a/b

def faktoriyel(a):
    print("Sonuç hesaplanıyor...")
    time.sleep(1)
    sonuc=1
    for i in range(1,a+1):
        sonuc*=i
    return sonuc

def karekok(a):
    print("Sonuç hesaplanıyor...")
    time.sleep(1)
    return a**0.5

