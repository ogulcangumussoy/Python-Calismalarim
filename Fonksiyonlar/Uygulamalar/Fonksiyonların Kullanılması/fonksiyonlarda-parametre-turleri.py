"""Normal şartlar altında parametreli fonksiyona parametre göndermezsek hata verir bunu çözmek için şu
yöntem kullanılır

//Normal Kullanım
def selamla(isim):
    print(isim)
selamla("Ahmet")

//Çıktısı selam isimsiz'dir.

def selamla(isim="isimsiz"):
    print("Selam",isim)
selamla()
selamla("Murat") // Şeklinde girilirse selam Murat der.

//Bilgileri goster fonksiyonu parametre olmazsa hata verir.
def bilgileriGoster(ad,soyad,numara):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)

bilgileriGoster("Ali Oğulcan","Gümüşsoy","123456")

//Bilgileri goster fonksiyonu parametre olmazsa hata vermez.

"""


def bilgileriGoster(ad="Isım Yok",soyad="Soyad yok",numara="Numara yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgileriGoster(ad="ali", numara="12345")

#print ile sıralı yazıdırırken araya boşluk yerine başka birşey koymak istersek

print("Ali","Oğulcan","Gümüşsoy",sep="/")
