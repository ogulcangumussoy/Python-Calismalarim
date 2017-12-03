"""
List comprehension kullanarak 1'den 100'e kadar olan sayıların sadece çift olanlarını bir listeye atın.
"""
liste = [x for x in range(1,101) if(x%2==0)]
print(liste)
