#Kwargs-items kullanımı

def fonksiyon(**kwargs):
    for i,j in kwargs.items(): #Sözlükte kelime ve anlamına tek tek erişimi sağlar.
        print("Argüman ismi",i,"Argüman Değeri",j)

fonksiyon(isim="Murat",soyisim="Coşkun",numara="123456")
