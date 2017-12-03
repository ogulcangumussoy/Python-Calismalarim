class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1

#kumanda objesini direk olarak iterator'a eşitlememiz gerekiyor.
    def __iter__(self): #bu metod ıterator oluşturmak için kullanılacak
        return self
    def __next__(self): #next metodu çağrılınca buraya girecek. self index -1'di ilk çalışmada 0 olacak
        self.index +=1 #index 0 oldu ilk çalışmada
        if self.index < len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration #liste index değeri aşılıca index'i -1 yapıp hata fırlattırdık.

kumanda = Kumanda(["Atv","Trt","Fox","Kanal D","Bloomberg"])
iterator = iter(kumanda)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
