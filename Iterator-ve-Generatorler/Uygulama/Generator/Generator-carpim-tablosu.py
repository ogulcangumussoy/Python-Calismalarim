#Generator kullanarak 1'den 10'a çarpım tablosu yapımı

def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpimtablosu(): #for döngüsü kendi içerisinde iterator kullanılıyordu. Boşuna bellek kullanmadan işlem yaptık.
    print(i)

#range() fonksiyonu genarator kullanılarak yapılmıştır
