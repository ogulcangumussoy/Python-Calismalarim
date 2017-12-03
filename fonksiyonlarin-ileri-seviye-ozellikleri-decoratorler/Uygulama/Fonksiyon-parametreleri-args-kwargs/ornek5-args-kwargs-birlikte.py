def fonksiyon(*args,**kwargs):
    for i in args:
        print(i)
    print("--------------")
    for i,j in kwargs.items():
        print(i,j)

fonksiyon(1,2,3,4,5,6,7,isim="Murat",soyisim="Coşkun",numara=123456)
