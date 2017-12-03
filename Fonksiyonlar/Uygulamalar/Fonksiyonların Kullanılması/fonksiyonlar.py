"""
Kod tekrarını engeller.
"""
def selamla(): # Fonksiyonun tanımlanması
    print("Merhaba")
    print("Nasılsınız?")

selamla() # Fonksiyonun kullanılması

def selamla(isim):
    print("İsminiz: ",isim)

selamla("Ali")

def toplama(a,b,c):
    print("Toplamları: ",a+b+c)

toplama(3,4,7)

def faktoriyel(sayi):
    faktoriyel=1
    if(sayi==0 or sayi==1):
        print("Faktoriyel: ",faktoriyel)
    else:
        while(sayi >=1):
            faktoriyel *=sayi
            sayi-=1

        print("Faktöriyel: ",faktoriyel)

faktoriyel(10)
