liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]

#sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] şeklinde yapmaya çalışalım

i=0
sonuc=list()
while(i<len(liste1) and i<len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i+=1
print(sonuc)

#bunu zip ile kısa yoldan yapabiliriz hazır kütüphane

print(list(zip(liste1,liste2)))
liste3=["python","java","php","javascript"]

print(list(zip(liste1,liste2,liste3)))


for i,j in zip(liste1,liste3):
    print(i,j)

#***********************************
#Sözlüklerin ziplenmesi
sozluk1={"Elma":1,"Armut":2,"Kiraz":3}
sozluk2={"Sıfır":0,"Bir":1,"İki":2}
print(list(zip(sozluk1,sozluk2)))
print(list(zip(sozluk1.values(),sozluk2.values())))
