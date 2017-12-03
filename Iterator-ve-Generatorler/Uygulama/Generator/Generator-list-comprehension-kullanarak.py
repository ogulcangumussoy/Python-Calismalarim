#list comprehension kullanımı (normal)
liste = [i*3 for i in range(5)]
print(liste)

#generator kullanarak list comprehension kullanımı

generator = (i*3 for i in range(5)) # tanımlamada fark köşeli değil düz parantez kullanılır.
iterator = iter(generator)
print(next(iterator))
