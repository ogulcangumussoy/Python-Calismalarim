import time
class Kullanicilar:
    def __init__(self,kullanici_adi="b1a2y3",ad="Ali Oğulcan",soyad="Gümüşsoy",parola=123,telefon_no=5515569450,email="ogulcangumussoy@gmail.com"):
        self.kullanici_adi=kullanici_adi
        self.ad=ad
        self.soyad=soyad
        self.parola=parola
        self.telefon_no=telefon_no
        self.email=email
    def kullanici_bilgileri_getir(self):
        print("""
        {} kullanici adindaki üyenin bilgileri:
            Ad: {}
            Soyad: {}
            Telefon No: {}
            E-Mail: {}
            Parola: {}
        """.format(self.kullanici_adi,self.ad,self.soyad,self.telefon_no,self.email,self.parola))
    def paroladegis(self,kullanicilar):
        print("""
        ********************
        Parola Değiştirme Ekranı
        *********************
        
        Kullanici Adiniz: {}
        Eski Parolaniz: {}
        """.format(self.kullanici_adi,self.parola))



    def bilgial(self):
        yeni_parola=input("Yeni Parolanız: ")
        parola_tekrar=input("Parola Tekrar: ")

        if(yeni_parola==parola_tekrar):
            print("Parolalar eşleşti. Değişim yapılıyor...")
            time.sleep(2)

            kullanicilar.parola=yeni_parola
        else:
            print("Parolalar eşleşmedi")
            return kullanicilar.bilgial()
        
while True:
    kullanicilar = Kullanicilar()
    kullanicilar.kullanici_bilgileri_getir()
    s=kullanicilar.bilgial()

    kullanicilar.kullanici_bilgileri_getir()
