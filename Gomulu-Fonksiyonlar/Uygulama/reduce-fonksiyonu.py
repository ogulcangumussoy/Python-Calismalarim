"""
Reduce fonksiyonu ikili toplama yapar şu şekilde gösterilebilir..
liste=a,b,c,d

sonuc=(((a+b)+c)+d)

"""
from functools import reduce #reduce fonksiyonunu import ettik
def toplama(x,y):
    return x+y
print(reduce(toplama,[12,18,20,10]))

#lambda kullanımı
print(reduce(lambda x,y:x*y,[1,2,3,4,5,6,]))

#**************
def maksimum(x,y):
    if(x>y):
        return x
    else:
        return y
print(maksimum(3,4))

#reduce kullanarak yapımı
print(reduce(maksimum,[-2,3,1,4])) #burda ikili karşılaştırarak sonuca ulaşır.
