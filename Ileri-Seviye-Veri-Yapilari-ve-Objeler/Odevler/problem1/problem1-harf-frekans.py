"""
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

"""

s="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb" #kelimemizi aldık
frekans=dict() #frekans adında bir sözlük oluşturduk.

for karakter in s: #s içerisinde geziniyoruz karakter i gibi bir değişken
    if(karakter in frekans): #karakter harfi frekans sözlüğünde varsa durumu
        frekans[karakter]+=1 #i. değerini 1 arttırdık. P:1 ' P'den bir tane var gibi
    else:
        frekans[karakter]=1

#yukarıda frekans sözlüğünün içerisini doldurduk. şimdi yazıralım i ve j ile kelime ve frekansını yazıracağız.

for i,j in frekans.items(): #sözlük içerisinde gezinmek için sozluk.items() yapısı kullanılır. in ile karşılaştırma yapılır.
    print(i,"harfinden",j,"tane var.")


