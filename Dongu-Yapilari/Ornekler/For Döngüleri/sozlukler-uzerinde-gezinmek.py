"""
Genel sözlük yapısı

sozluk = {"bir":1, "iki":2, "üç":3, "dört":4}

sozluk.keys() //Bunun çıktısı
dict_keys(['bir', 'iki', 'üç', 'dört']) //şeklindedir.

sozluk.values() //Bunun Çıktısı
dict_values([1, 2, 3, 4]) //şeklindedir.

sozluk.items() //   Bunun çıktısı
dict_items([('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4)]) //şeklindedir.


"""
sozluk ={"bir":1,"iki":2,"üç":3,"dört":4}
#keyleri yazdırmak için

for eleman in sozluk:
    print(eleman)
for eleman2 in sozluk.values():
    print(eleman2)
for i,j in sozluk.items():
    print("Anahtar: {} Değer: {}".format(i,j))
