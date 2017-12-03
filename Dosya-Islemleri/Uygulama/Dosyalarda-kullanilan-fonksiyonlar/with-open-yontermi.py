"""
Close bazen unutabiliyor bu yöntem kendi içinde bu işlemi yapıyor.
"""
with open("../Bilgiler.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i,end="")
