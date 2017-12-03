"""
r+: hem okuma hem de yazma imkanı verir.
"""
with open("../Bilgiler.txt","r+",encoding="utf-8") as file:
    file.seek(10) #10.byte gittik.
    file.write("Deneme121212")
    file.seek(0)
    print(file.read())
