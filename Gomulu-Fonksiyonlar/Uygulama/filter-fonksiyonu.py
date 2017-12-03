#print(list(filter(lambda x: x%2 == 0,[1,2,3,4,5,6,7,8]))) #bir şarta göre filtreleme yaptık

def asal_mi(x):
    i=2
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        while(i<x):
            if(x%i ==0):
                return False
            i +=1
        return True
while True:
    sayi=input("Sayı giriniz: ")
    if(sayi=="q"):
        break
    else:
        sayi=int(sayi)
        print(asal_mi(sayi))
        print(list(filter(asal_mi,range(1,100))))
