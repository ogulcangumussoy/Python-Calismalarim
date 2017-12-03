"""
Iterator nedir?
Üzerinde gezilebilecek objelerdir.
Python'da üzerinde gezebildiğimiz tüm objeler bir iterable objedir. Örneğin demetlerden,listelerden,stringlerden
oluşturduğumuz bütün objeler iterable bir objedir.


Iterator oluşturma

Bir iterator objesini,iterable bir objeden(liste,demet,string vs.) oluşturmak için Python'da iter() fonksiyonunu
kullanıyoruz. Ve bu objenin bir sonraki elemanını almak için next() fonksiyonunu kullanıyoruz.
"""

liste= [1,2,3,4,5] #liste oluşturduk (iterable obje)
iterator = iter(liste) #iterator değişkeni ile listemizi iterator'a attık
print(next(iterator)) #sonucu 1 çıkar ilk eleman
print(next(iterator))#sonucu 2 çıkar
print(next(iterator))#sonucu 3 çıkar
print(next(iterator)) #sonucu 4 çıkar
print(next(iterator)) #sonucu 5 çıkar

#Bu iteratorler for döngülerinde kullanılıyor otomatik olarak
"""
liste= [1,2,3,4,5,6]
    for i in liste:
        print(i)
şeklinde kullanımda iteratorler arka planda kullanılır.
"""
#for döngüsü mantığı bu şekilde
iterator=iter(liste)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
