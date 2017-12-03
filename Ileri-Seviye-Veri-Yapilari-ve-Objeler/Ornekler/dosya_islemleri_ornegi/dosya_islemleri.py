class Dosya():

    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi=file.read() #dosya iceriğini aldık

            kelimeler=dosya_icerigi.split() #boşluğa göre parçaladık ve kelimeler listesine attık.
            self.sade_kelimeler=list() #self ile class'ın elemanı olduğunu belirttik diğer yerlerde kullanmak için

            for i in kelimeler:
                #burada \n, boşluk, nokta ve virgül olan yerleri kes dedik.
                i=i.strip("\n")
                i=i.strip(" ")
                i=i.strip(".")
                i=i.strip(",")

                self.sade_kelimeler.append(i) #sadeleşmiş kelimeleri döngü içinde ekleme yaptık.

    def tum_kelimeler(self):
        kelimeler_kumesi= set()

        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i) #kümeye ekleme yaptık.

        print("Tüm kelimeler............")

        for i in kelimeler_kumesi:
            print(i)
            print("***********************")

    def kelime_frekans(self):
        kelime_sozluk= dict()

        for i in self.sade_kelimeler:

            if (i in kelime_sozluk): #kelime sözlüğümüzde şu anda var mı dedik
                kelime_sozluk[i] += 1 #varsa 1 arttır.

            else:
                kelime_sozluk[i] = 1  #yoksa da ilk kez olduğu için 1 yazıyoruz.

        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geçiyor....".format(kelime,sayi))

            print("---------------------------------------")

dosya=Dosya()
dosya.kelime_frekans()
