try:
    file= open("../Bilgiler.txt","r",encoding="utf-8")
    for i in file:
        print(i,end="")#Ekstra boşluk bırakmasını engeller varsayılan "\n"
    file.close()
except FileNotFoundError:
    print("Dosya Bulunamadı")
