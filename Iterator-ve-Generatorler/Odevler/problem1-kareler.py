"""
'Kareler' isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init fonksiyonu
maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi
yazdırılsın. StopIteration hatası ekrana maksimum sayıyı geçtiğimiz zaman fırlatılsın
"""

class Kareler():

    def __init__(self,maksimum):
        self.maksimum = maksimum
        self.sayi = 1

    def __iter__(self):
        return self
    def __next__(self):

        if(self.sayi <= self.maksimum):
            sonuc = self.sayi**2
            self.sayi +=1
            return sonuc
        else:
            self.sayi=0
            raise StopIteration


kareler = Kareler(5)
for i in kareler:
    print(i)
