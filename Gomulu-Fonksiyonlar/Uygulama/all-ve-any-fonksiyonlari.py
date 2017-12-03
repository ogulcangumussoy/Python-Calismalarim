def hepsi(liste): #herhangi bir değer de false varsa false döndürür.
    for i in liste:
        if not i: #not i demekle i'nin false olma durumunu alıyoruz.
            return False
    return True
liste= [True,False,True,False,True]
print(hepsi(liste))
liste1=[1,2,3,4,5,6,7] #sayılarda 0 hariç tüm sayılar true dir.
print(hepsi(liste))

def herhangi(liste): #herhangi bir true varsa true basar
    for i in liste:
        if i:
            return True
    return False
print(herhangi(liste))
liste3=[0,0,0,0,0]
print(herhangi(liste3))

#Bu yöntemleri kısa yolda yapmak için all ve any fonksiyonları kullanılabilir.

print(all(liste)) #tüm değerler true ise true basar
print(all([True,True,True,True])) #hepsi true olduğu için true basar.

print(any([True,False,True,False,True])) #herhangi true ise true basar hepsi false ise false basar
