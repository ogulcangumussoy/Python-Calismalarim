"""
Decorator fonksiyonlar,Python'da fonksiyonlarımıza dinamik olarak ekstra özellik eklediğimiz fonksiyonlardır ve decorator
fonksiyonların kullanımı kod tekrarı yapmamızı engeller. Python'da decorator fonksiyonlar Flask gibi frameworklerde oldukça
fazla kullanılır.
"""

import time #fonksiyonların ne kadar sürdüklerini hesaplayacağız.
def zaman_hesapla(func):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc= func(sayilar)
        bitis = time.time()
        print(func.__name__+" "+str(bitis-baslama)+"saniye sürdü.")
        return sonuc
    return wrapper
@zaman_hesapla
def kareleri_hesapla(sayilar):
    sonuc=list()
    #baslama = time.time() #decorator olmadan
    for i in sayilar:
        sonuc.append(i ** 2)
    #bitis= time.time() #decorator olmadan

    #print("Bu fonksiyon",str(bitis-baslama)," saniye sürdü")#decorator olmadan
    return sonuc
@zaman_hesapla
def kupleri_hesapla(sayilar):
    sonuc=list()
    #baslama= time.time()#decorator olmadan
    for i in sayilar:
        sonuc.append(i ** 3)
    #bitis= time.time()#decorator olmadan
    #print("Bu fonksiyon ",str(bitis-baslama)," saniye sürdü")#decorator olmadan
    return sonuc

kareleri_hesapla(range(100000))
kupleri_hesapla(range(100000))
