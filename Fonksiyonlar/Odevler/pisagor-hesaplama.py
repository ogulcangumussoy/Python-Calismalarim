"""
1'den 100' kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın (a<=100,b<=100)
"""
print("""Pisagor Tablosu""")

def pisagorHesapla():
    pisagor_listesi=list()
    for i in range(1,101):
        for j in range(1,101):
            c=(i**2+j**2)**0.5
            if(c==int(c)):
                pisagor_listesi.append((i,j,int(c)))

    return pisagor_listesi

for i in pisagorHesapla(): #zaten bize bir liste döndürüyor içinde bu şekilde gezebiliriz.
    print(i)
