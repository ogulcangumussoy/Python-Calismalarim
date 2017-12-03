"""
Modüller kullanıcıya kolaylıklar sağlar. Amerikayı yeniden keşfetmeye gerek yok.
"""
import math #modülü içeri aktarma işlemi yapıldı.

print(math.factorial(5)) #faktöriyel metodunu kullanıp değeri hesapladık.

print(math.floor(5.6)) #alta yuvarlama

print(math.ceil(5.6)) #üste yuvarlama

import math as matematik #kütüphaneyi farklı isimde import ettik..

print(matematik.factorial(5))

from math import * # math içerisindeki tüm fonksiyonları alıyoruz.

factorial(5) #bunun farkı math.factorial demeye gerek kalmaması
floor(6.4)

#ya da sadece iki fonksiyon dahil etmek için

from math import floor,ceil
floor(5.6)
