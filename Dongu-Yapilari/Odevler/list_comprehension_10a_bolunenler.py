"""
list comprehension kullanarak 1-100 arası 10 a bölünenler i listele. (2,5) Beraber kullanıldığını görmek için uzun yazıldı
"""
liste = [x for x in range(1,101) if(x%5==0) if(x%2==0)]
print(liste)
