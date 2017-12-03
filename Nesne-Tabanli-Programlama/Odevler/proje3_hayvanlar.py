class Hayvan:
    def __init__(self,ad,ayak_sayisi,ses,ucabilme):
        self.ad=ad
        self.ayak_sayisi=ayak_sayisi
        self.ses=ses
        self.ucabilme=ucabilme
    def __str__(self):
        return "{} adındaki hayvanın:\n{} tane ayağı vardır.\nSesi '{}' şeklindedir.\nUçabilme Özelliği {}".format(self.ad,self.ayak_sayisi,self.ses,self.ucabilme)
    def __len__(self):
        return "{} adındaki hayvanın {} ayağı vardır.".format(self.ad,self.ayak_sayisi)

class Kopek(Hayvan):
    def __init__(self,ad,ayak_sayisi,ses,ucabilme,isirma):
        super().__init__(ad,ayak_sayisi,ses,ucabilme)
        self.isirma=isirma
    def __str__(self):
        return "{} adındaki hayvanın:\n{} tane ayağı vardır.\nSesi '{}' şeklindedir.\nUçabilme Özelliği: {}\nIsırabilme:{}\n".format(self.ad,self.ayak_sayisi,self.ses,self.ucabilme,self.isirma)

class Kus(Hayvan):
    def __init__(self,ad,ayak_sayisi,ses,ucabilme,yumurtlama):
        super().__init__(ad,ayak_sayisi,ses,ucabilme)
        self.yumurtlama=yumurtlama
    def __str__(self):
        return "{} adındaki hayvanın:\n{} tane ayağı vardır.\nSesi '{}' şeklindedir.\nUçabilme Özelliği: {}\nYumurtlama:{}\n".format(self.ad,self.ayak_sayisi,self.ses,self.ucabilme,self.yumurtlama)

class At(Hayvan):
    def __init__(self,ad,ayak_sayisi,ses,ucabilme,kisneme):
        super().__init__(ad,ayak_sayisi,ses,ucabilme)
        self.kisneme=kisneme
    def __str__(self):
        return "{} adındaki hayvanın:\n{} tane ayağı vardır.\nSesi '{}' şeklindedir.\nUçabilme Özelliği: {}\nKisneme:{}\n".format(self.ad,self.ayak_sayisi,self.ses,self.ucabilme,self.kisneme)

kopek = Kopek("Köpek","4","Hav","Yok","Var")
print(kopek)
at = At("At","4","(Kişneme Sesi)","Yok","Var")
print(at)
