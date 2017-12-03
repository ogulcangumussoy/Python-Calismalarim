class Araba:
    def __init__(self,marka="yok",model="2005",renk="kirmizi",yil=2010):
        self.marka=marka
        self.model=model
        self.renk=renk
        self.yil=yil

araba1=Araba(marka="Ferrari")
print(araba1.marka)

araba2=Araba
araba2.yil=2015
print(araba2.yil)


