"""
Python'da __init__ ,  __str__ , __len__ vb. fonksiyonlar var biz bunları override edip değerlerini bastırabiliriz.
"""

class Kitap:

    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayisi=sayfa_sayisi
        self.tur=tur
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı:{}\nTürü: {}\n".format(self.isim,self.yazar,self.sayfa_sayisi,self.tur)

    def __len__(self):
        return self.sayfa_sayisi
    def __del__(self):
        print("Kitap objesi siliniyor.........")

kitap = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye") # __init__ fonksiyonunun içerisine veri girdik.
print(kitap) # __str__ fonksiyonu çalışır normal şartlarda olarak onada değer verdik direk onları yazdı.
print(len(kitap)) # __len__ metodunu kullandık
del kitap #python __del__ kütüphanesini kullandık.
print(kitap) #artık kitap nesnesi bulunamaz. Silindi..
