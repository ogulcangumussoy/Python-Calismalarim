class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller

    def bilgileriGoster(self):
        print("""
        Yazılımcı Objesinin Özellikleri
        
        İsim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Bildiği Diller: {}     
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
    def zam_yap(self,zam_miktari):
        print("Zam Yapılıyor...")

        self.maas += zam_miktari
    def dil_ekle(self,yeni_dil):
        print("Dil Ekleniyor...")
        self.diller.append(yeni_dil)

yazilimci = Yazilimci("Ali Oğulcan","Gümüşsoy",12345,3000,["Python","Java","C","Javascript"])
yazilimci.dil_ekle("C#")
yazilimci.zam_yap(500)
yazilimci.bilgileriGoster()
