"""
 __init__(self) şeklinde bir kullanımı var bu olmazsa override edemeyiz ilk parametre sabit olarak self olur.
 sorasında istediğimiz değişkenleri tanımlıyoruz.
 self.model = model ile kullanıcıdan gelenle içerdeki değerleri eşitliyoruz.
  def __init__(self,model="Bilgi Yok",renk="Bilgi Yok",beygir_gucu=70...) Burda tanımla yaparken default değerde verdik
  vermek zorunda değiliz. Eğer değer girilmezse bu default değerleri kabul ediliyor.

    araba = Araba(beygir_gucu=110) bu kullanımda ise bir nesne oluşturup sadece beygir gücüne değer verdik 70 den 110 oldu
    diğer değerleri default olacak.
"""
class Araba():


    def __init__(self,model="Bilgi Yok",renk="Bilgi Yok",beygir_gucu=70,silindir=4): #self olmak zorunda. This kullanımına benziyor
        print("init fonksiyonu çağırıldı.")
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir =silindir

#araba1=Araba("Renault Megane","Gümüş",110,4) #Nesne oluşturma değer girilirken self girilmez.
#araba2=Araba("Peugeot","Beyaz",90,4)

araba = Araba()
araba.renk="mavi"

print(araba.model)
print(araba.renk)
