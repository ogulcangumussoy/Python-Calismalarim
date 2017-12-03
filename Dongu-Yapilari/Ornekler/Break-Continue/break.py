"""
Döngü herhangi bir anda break ile karşılaştığında anında kayboluyor. Sadece içindeki bulunduğu
döngüyü sonlandırır.

"""
i=0
while (i<10):
    if(i == 5):
        break
    print("i",i)
    i+=1
