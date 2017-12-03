liste= [1,2,3,4,5]
liste.append(6) #listeye append ile '6' elemanını ekledik.
liste.append("Python")#Listeye string eklemesi de yapabildik.
print(liste)

liste1= [1,2,3,4,5,6,7]
liste2=[10,20,30]

liste1.extend(liste2) #liste1'e liste2'yi attık. Çoklu append denebilir.
print(liste1)

liste=[1,2,3,4,5,6,7,8,9]
liste.insert(2,"Python") #insert ile indis nosuna göre listeye ekleme yapabiliriz.

liste=[1,2,3,4,5,6,7]
liste.pop() #eğer içerisine değer girmezsek son elemanı çıkarır.
liste.pop(2) #ikinci indisteki değeri listeden çıkarır.

liste=["Python","Php","Java","C"]
liste.remove("Python") #remove komutunda direk olarak elemanının değerini giriyoruz. Eğer eleman yoksa hata verir.

#index metodu verilen bir değerin baştan başlarak hangi indiste olduğunu söyler. İndex değeri ile yazılırsa o değerden
#itibaren arama yapar.
liste=[1,2,3,4,3,3,3,5,6,7,8,9]
print(liste.index(3))#ilk olarak 2.indiste kullanılmış.
print(liste.index(3,3)) #3 değerini arıyoruz ve 3.indisten itibaren arıyoruz demek.
# İndex de eğer olmayan değer verirsek ValueError hatası verir.

liste=[1,2,3,3,4,5,6,7,3,3,3,3]
print(liste.count(3)) #listede '3' değeri kaç kere geçiyor diye döndürüyor.

liste2=[12,-2,3,1,34,100]
liste=liste2.sort(reverse=True)
print(liste)

liste= ["Python","Php","Java","C"]
print(liste.sort(reverse=True))

