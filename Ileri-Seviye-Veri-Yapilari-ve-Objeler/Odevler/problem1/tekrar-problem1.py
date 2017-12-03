s="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans=dict()

for karakter in s:
    if(karakter in frekans): #karakter frekans içerisinde var mı?
        frekans[karakter]+=1
    else:
        frekans[karakter]=1

#yazdırma işlemi
for i,j in frekans.items():
    print(i,"harfinden",j,"tane var.")
