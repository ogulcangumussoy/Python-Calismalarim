"""
Elimzde şöyle bir liste bulunsun
    [1,2,3,4,5,6,7,8,9,10]
Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın
NOT: İlk önce filter() ile çift sayıları ayıklayın.Daha sonra reduce() fonksiyonunu kullanın.
"""
from functools import reduce
liste=[1,2,3,4,5,6,7,8,9,10]
filtrele= list(filter(lambda x:x%2==0,liste))
print(reduce(lambda x,y: x+y,filtrele))
