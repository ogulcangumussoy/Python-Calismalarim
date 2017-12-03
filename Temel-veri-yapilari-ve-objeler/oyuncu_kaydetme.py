print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı: ")
soyad= input("Oyuncunun Soyadı: ")
takim = input("Oyuncunun Takımı: ")

#Bilgileri bir listeye atalım.

bilgiler = [ad,soyad,takim]

print("Bilgiler kaydediliyor...")

print("Oyuncu Adi: {}\nOyuncu Soyadı:{}\nOyuncunun Takımı:{}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]));

print("Bilgiler Kaydedildi......")
