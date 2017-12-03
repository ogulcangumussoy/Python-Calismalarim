def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def anafonksiyon(func1,func2,func3,func4,islem_adi):
    if islem_adi=="toplama":
        print(func1(3,4))
    elif islem_adi=="cikarma":
        print(func2(10,3))
    elif islem_adi=="carpma":
        print(func3(3,5)) #eşleşmeye göre func3 carpma demek carpma(3,5) oluyor.
    elif islem_adi=="bolme":
        print(func4(10,4))
    else:
        print("Geçersiz İşlem...")

anafonksiyon(toplama,cikarma,carpma,bolme,"toplama") #"" işareti olmadan fonksiyonları yolluyoruz.
anafonksiyon(toplama,cikarma,carpma,bolme,"bolme")
