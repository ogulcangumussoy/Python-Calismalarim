"""
Bu fonksiyonun amacı
liste=["Elma","Armut","Kiraz"]
şeklinde bir listeyi

(0,'Elma')(1,'Armut').. şeklinde indislerle birlikte yazmak.
Bunun uzun yolu aşağıdaki gibidir..
"""
liste=["Elma","Armut","Muz","Kiraz"]
i=0
sonuc=list()
while(i<len(liste)):
    sonuc.append((i,liste[i]))
    i+=1
print(sonuc)

#Bunun kısa yoldan yapmak için enumarete fonksiyonudur.
print(list(enumerate(liste)))
for i,j in enumerate(liste):
    print(i,j)

#Başka bir kullanım örneği Burada çift indisli harfleri yazdırdık.
liste=["a","b","c","d","e","f","g"]
for i,j in enumerate(liste):
    if(i%2==0):
        print(j)
