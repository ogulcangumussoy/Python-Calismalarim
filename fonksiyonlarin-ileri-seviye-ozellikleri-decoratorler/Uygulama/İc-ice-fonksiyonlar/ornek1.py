def selamla(isim):
    print("Selam",isim)

selamla("Ayşe")
merhaba=selamla #fonksiyonu başka bir değişkene attık
merhaba("Kemal")  #artık merhaba'dan da selamla fonksiyonunu çağırabiliyoruz.

del selamla #selamla objesini sildik
merhaba("Ali") #ama merhaba halen selamla fonksiyonu gösteriyor.


def fonksiyon():

    def fonksiyon2(): #bu fonksiyona dışarıdan erişemeyiz fonksiyonun içerisinde local
        print("Küçük fonksiyondan herkese merhaba")

    fonksiyon2()
    print("Büyük fonksiyondan herkese merhaba")

fonksiyon()


