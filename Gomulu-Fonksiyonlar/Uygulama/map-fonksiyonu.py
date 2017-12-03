def double(x):
    return x*2
liste=list(map(double,[1,2,3,4,5,6,7])) #map fonksiyonu kendi içinde for döngüsüne sahip gibi çalışıyor tüm elemanlarını
                                #tek tek fonksiyona sokuyor. List ile de sonucu liste içine aldık.
print(liste)

#********Bunu lambda ile de yapabiliriz*****************

liste2=list(map(lambda x:x**2,(1,2,3,4,5,6,7,8,9,10))) #lambda da fonksiyon yazabiliyoruz x leri x**2 ile değiştir dedik.
print(liste2)

#*******İki listeyi ve üç listeyi lambda ile çarpmak map kullanarak*********
list1=[1,2,3,4]
list2=[5,6,7,8]
list3=[9,10,11,12,13]

listeIkili= list(map(lambda x,y:x*y,list1,list2))
print(listeIkili)

listeUclu= list(map(lambda x,y,z:x*y*z,list1,list2,list3))
print(listeUclu)
