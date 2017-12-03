"""
Bir dosyayı açmak için "open()" fonksiyonunu kullanıyoruz. Yapısı şu şekildedir.
        open(dosya_adi,dosya_erisme_kipi)
"w" dosya kipi
Dosyalarımızı açmak ve dosyalarımıza yazmak için "write" yani "w" kullanılır. Eğer oluşturmak istediğimiz dizinde
o dosya yoksa oluşturur varsa da silip tekrardan oluşturur.

file=open("Bilgiler.txt","w",encoding="utf-8")
file.write("Ali Oğulcan Gümüşsoy2")
file.close()
file=open("Bilgiler.txt","w",encoding="utf-8")#tekrardan yazınca öncekini siler üstüne yazar.
file.close()
"""
#a kipi(append)
"""
file=open("Bilgiler.txt","a",encoding="utf-8")
file.write("Veli Deli")
file.close()

"""
file=open("Bilgiler.txt","a",encoding="utf-8")
file.write("Yapılacaklar:\n")
file.close()
file=open("Bilgiler.txt","a",encoding="utf-8")
file.write("Python Eğitimi")
file.close()

