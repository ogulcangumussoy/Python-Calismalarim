with open("mailler.txt","r",encoding="utf-8") as file:
    for satir in file:
        satir= satir[:-1]
        if(satir.endswith(".com") and satir.find("@") != -1):
            print(satir)
