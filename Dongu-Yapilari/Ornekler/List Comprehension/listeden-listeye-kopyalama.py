"""
List Copmprehension

Bu konuda listeleri üretmek ve oluşturmak Python'da çok pratik bir yöntem olan "List Comprehension" konusunu
öğreneceğiz.

liste= [1,2,3,4]
liste.append(5)
print(liste)

"""
liste1 = [1,2,3,4,5]

liste2= list() #Boş Liste

for i in liste1:
    liste2.append(i)

print(liste2)
