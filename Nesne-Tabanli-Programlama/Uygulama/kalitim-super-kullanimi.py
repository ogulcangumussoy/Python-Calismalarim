class Calisan:
    def __init__(self,isim,maas,departman):
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgileriGoster(self):
        print("Çalışan Sınıfının bilgileri\nİsim: {}\nMaaş:{}\nDepartman:{}".format(self.isim,self.maas,self.departman))
    def departmanDegistir(self,yeni_departman):
        self.departman=yeni_departman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        super().__init__(isim,maas,departman) #super ile calisan içinden direk aldık diğerlerini
        self.kisi_sayisi=kisi_sayisi #ekstradan tanımlama yaptık.
    def bilgileriGoster(self):
        print("Yönetici Sınıfının bilgileri\nİsim: {}\nMaaş:{}\nDepartman:{}\nSorumlu Kisi Sayisi: {}".format(self.isim,self.maas,self.departman,self.kisi_sayisi))
    def zam_yap(self,zam_miktari):
        self.maas=+zam_miktari
isim = input("Adınız: ")
maas= int(input("Maaşınız: "))
departman = input("Bölümünüz: ")
kisi_sayisi= int(input("Sorumlu Kişi Sayısı: "))
calisan = Calisan(isim,maas,departman)
calisan.bilgileriGoster()
yonetici = Yonetici(isim,maas,departman,kisi_sayisi)
yonetici.bilgileriGoster()
