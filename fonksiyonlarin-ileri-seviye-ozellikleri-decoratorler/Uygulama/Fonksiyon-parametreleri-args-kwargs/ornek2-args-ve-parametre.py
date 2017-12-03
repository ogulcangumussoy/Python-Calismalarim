#Args ile normal parametrenin birlikte kullanımı

def fonksiyon(isim,*args):
    print("İsim",isim)
    print("-------------------")
    for i in args:
        print(i)
fonksiyon("Murat",1,2,3,4,5,6,7,8) #Murat ile isim eşleşti geri kalanları args olarak yazdık.
