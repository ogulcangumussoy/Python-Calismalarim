#Os modülü işletim sistemi ile ilgili işlemler yapabilmemiz için oluşturulan kütüphane

import os
from datetime import datetime
print(dir(os)) #Os modülü içerisindeki fonksiyonları gösterir.
os.chdir("/home/ogulcan/Desktop") #Dizini değiştirdik

print(os.listdir()) #Bulunduğumuz dizindeki dosyaları listeler liste halinde

for i in os.listdir():
    print(i) #listeyi yazdırdık.
print(os.getcwd()) #Bulunduğumuz dizini verir.

os.mkdir("Deneme5") #Bulunduğumuz dizinde bir klasör oluşturdu
os.makedirs("Deneme2/Deneme3/Deneme4") #iç içe dosya oluşturur
os.rmdir("Deneme2/Deneme3/Deneme4") #bir dosyayı silmeye yarar
os.removedirs("Deneme2/Deneme3") # Deneme2 ve Deneme3 ü sildi

os.rename("sd","test2") #sd adındaki bir nesnenin adını değiştirdi


print(os.stat("test2.txt")) #burda test2.txt içerisindeki detaylı bilgileri verdi oluşturma zamanı vb.
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) #st_mtime adındaki değişkeni verdi.
#datetime.fromtimestap ile de milisaniye formatında gelen sayiyi tarih formatına çevirdik.

for i in os.walk("/home/ogulcan/Desktop"): #os.walk ile bir dizin altındaki tüm dosya ve klasörlere ulaşabiliriz.
                                           #Bize genarator nesnesi oluşturuyor for ile içinde gezebiliriz.
     print(i)

#Çıktıyı güzelleştirmek için
for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("/home/ogulcan/Desktop"):
     print("Klasör Yolu",klasor_yolu)
     print("Klasör İsimler",klasor_isimleri)
     print("Dosya İsimleri",dosya_isimleri)
     print("*************************************")

#Sadece dosya adlarını yazdırmak için
for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("/home/ogulcan/Desktop"):
    for i in dosya_isimleri:
        print(i)
#bir değere göre listeleme yapma tüm pdfleri yazdırdık
for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("/home/ogulcan/Desktop"):
    for i in dosya_isimleri:
        if(i.endswith(".pdf")):
            print(i)
