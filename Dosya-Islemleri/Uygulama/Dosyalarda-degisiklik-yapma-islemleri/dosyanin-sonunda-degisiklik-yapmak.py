with open("../Bilgiler.txt","a",encoding="utf-8") as file:
    file.write("Semih Aktaş\n")
with open("../Bilgiler.txt","+r",encoding="utf-8") as file:
    print(file.read())
