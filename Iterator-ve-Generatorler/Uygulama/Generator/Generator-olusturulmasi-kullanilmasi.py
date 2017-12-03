"""
Genartorler bellekte yer kaplamazlar. Örnek vermek gerekirse for döngüsü ile 100.000 tane
değeri yazdırmak bellekte çok yer kaplar çünkü listeyi bir değişkenle bellekte tutmamız gerekir
Genarator de ise liste oluşturmaya gerek kalmaz 'yield' yapısı ile o anda oluşturup basarız
ve o değer bir daha erişilemez. Bu şekilde bellekte yer işgal etmez.
"""

#ilk olarak iterator kullanmadan kareleri al metodunu yazalım

def kareleri_al():
    sonuc= []

    for i in range(0,6):
        sonuc.append(i ** 2)
    return sonuc

print(kareleri_al())

#Şimdi ise genarator kullanalım bunun için sonuc listesi kullanmayacağız sadece yield var

def kareleri_al():
    for i in range(0,6):
        yield i**2


generator = kareleri_al() #Burada değerler henüz yüklenmedi içi boş
iterator = iter(kareleri_al())
print(next(iterator)) #genarator bana erişilmek istiyor ilk değerimi üreteyim diyor. Şu anda metodun içerindeki
                    # diğer değerler üretilmedi
print(next(iterator)) #artık ilk değer silindi ulaşılamaz durumda

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) #son değeri aştığı için hata basar genarator artık kullanılamaz durumda

iterator2=iter(generator)
print(next(iterator)) #dediğimizde aynı hatayı basar genarator artık işlevini yitirdi yeniden oluşturmak gerekiyor.

