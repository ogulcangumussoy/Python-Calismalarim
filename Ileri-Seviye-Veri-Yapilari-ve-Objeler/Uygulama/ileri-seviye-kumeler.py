"""
Kümeler matematikte olduğu gibi bir elemandan sadece bir tane tutan bir veri tipidir. Bu açıdan kullanıldıkları yerlerde
çok önemli bir veri tipi olmaktadırlar.
"""

#*********Küme oluşturma*************
x={1,2,3}
print(type(x)) #çıktısı set'tir yani küöe

x = set() #küme tanımlama

liste = [1,2,3,4,5,3,3,1,1,2,2,2,2]
x=set(liste) #Her elemandan bir tane var
print(x)

#Eğer içerisine bir string gönderirsek her karakterden bir tane olacak şekilde çıktı verir.

x=set("Python Programlama dili")
print(x)

x={"Python","Php","Phyton"} #çıktısı {'Php','Phyton'} şeklindedir.
print(x)

#*********For Döngüsü ile Gezinme

x={"Elma","Armut","Kiraz","Muz"} #küme ve sözlükler sırasızdır.

for i in x:
    print(i)

x={"Python","Php","Java","Javascript"}
#x[0] #hata verir indisler yok

liste= list(x) #listeye çevirip indisle alabildik.
for i in liste:
    print(i)
print(liste[0])

#*******Eleman Ekleme*************
y={1,2,3,4,5,6}
y.add(8) #y' ye eleman eklemek için add kullandık eğer eleman varsa hata vermez.
print(y)

#*******Kümeler arasındaki farkı bulma********

kume1={1,2,3,10,34,100,-2}
kume2={1,2,23,34,-1}
print(kume1.difference(kume2)) #iki kume arasındaki farklar kume1 de olup kume 2 de olmayanlar.
print(kume2.difference(kume1))

#**********Difference_update(x) metodu ile iki kume arasındaki farkı bir kümeye atma********
kume1.difference_update(kume2)
print(kume1)#küme1'in değeri artık kume1//kume2


#Kümeden eleman çıkarma için= discard(x) x değerini kümeden çıkar demek eğer yoksa hata vermez.


x={1,2,3,4,5,6}
x.discard(5)
print(x) #çıktı : {1,2,3,4,6}



#Kümelerin Kesişimi

kume1={1,2,3,4,100,200,34,-2}
kume2={1,2,3,24,34,-1}

print(kume1.intersection(kume2)) #iki kümenin kesişimi


#Intersection_update() --> bu metod ise birinci kümeyle ikinci kümenin kesişimini bulur ve birinci kümeyi bu kesişime göre
#düzenler.

kume1={1,2,3,4,100,200,34,-2}
kume2={1,2,3,24,34,-1}
kume1.intersection_update(kume2)
print(kume1) # çıktı olarak {1,2,3,34}  verir.


#isdisjoint: Ayrık küme kontrolü yapar.
kume1={1,2,3,4,100,200,34,-2}
kume2={1,2,3,24,34,-1}
kume3={30,40,50}

print(kume3.isdisjoint(kume1)) #sonuç true döner.

#issubset(x) Alt Küme olup olmadığını kontrol eder.
kume1={1,2,3}
kume2={1,2,3,4}
kume3={5,6,7}
print(kume1.issubset(kume2))

#*******************İKİ KÜMENİN BİRLEŞİMİNİ ALMA******************************

kume1={1,2,3,4,100,200,34,-2}
kume2={1,2,3,24,34,-1}

print(kume1.union(kume2))
kume1.update(kume2) #iki kümenin birleşimini al kume1'e at.
