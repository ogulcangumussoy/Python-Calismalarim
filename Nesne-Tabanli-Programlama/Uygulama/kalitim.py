class Calisan:

    def __init__(self,isim,maas,departman):
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileri....")
        print("İsim:{}\nMaas:{}\nDepartman:{}\n".format(self.isim,self.maas,self.departman))
    def departmanDegistir(self,yeni_departman,zam_miktari):
        self.departman=yeni_departman
        zam_miktari=int(zam_miktari)
        self.maas+=zam_miktari
        return yonetici.bilgileriGoster()

class Yonetici(Calisan): #Extends kullanımı
    #pass #İçeriği sonra doldurulacak demek
    def zamYap(self,zam_miktari):
        self.maas+=zam_miktari

isim=input("İsminiz: ")
maas=int(input("Maaşınız: "))
departman= input("Departmanınız: ")
yonetici=Yonetici(isim,maas,departman)
yonetici.bilgileriGoster()
terfi=input("Terfi edildiyseniz '1' yazınız: ")
if(terfi=="1"):
    bolum=input("Terfi edildiğiniz alan: ")
    zam=input("Maaşınız ne kadar değişti? :")
    yonetici.departmanDegistir(bolum,zam)

