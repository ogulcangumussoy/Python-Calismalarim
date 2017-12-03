"""Gelen 2 basamaklı sayının okunuşunu yazan program"""
birler=["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar=["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
def okunus(sayi):
    birinci= sayi%10
    ikinci=sayi//10
    return onlar[ikinci]+" "+birler[birinci]
print("""
*******************************
İki basamaklı sayının Okunuşunu Öğrenme Programı
(Çıkmak için 'q' ya basınız...)
*******************************""")
while True:
   sayi=input("Sayınızı giriniz: ")
   if(sayi=="q"):
       print("Programdan çıkılıyor.")
       break
   else:
       sayi=int(sayi)
       print(okunus(sayi))
