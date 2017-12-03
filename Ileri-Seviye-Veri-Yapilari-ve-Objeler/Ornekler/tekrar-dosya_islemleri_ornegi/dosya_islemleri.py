class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi= file.read() #dosya icerigi alındı.

            #icerisindeki boşlukları sil
            kelimeler= dosya_icerigi.split()
            #her yerden ulaşılabilir bir değişken tanımla
            self.sade_kelimeler=list()
            for i in kelimeler:
                i=i.strip("\n")
                i=i.strip(" ")
                i=i.strip(".")
                i=i.strip(",")
                self.sade_kelimeler.append(i)

    def tum_kelimeler(self):
        kelimeler_kumesi=set() #küme oluşturduk.

        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        print("Tüm Kelimeler............")
        for i in kelimeler_kumesi:
            print(i)
            print("****************")

    def kelime_frekans(self):
        kelime_sozluk=dict() #sözlük oluşturduk

        for i in self.sade_kelimeler:
            if(i in kelime_sozluk):
                kelime_sozluk[i]+=1
            else:
                kelime_sozluk[i]=1
        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geçiyor....".format(kelime,sayi))
            print("------------------------------------")

dosya= Dosya()
dosya.kelime_frekans()

