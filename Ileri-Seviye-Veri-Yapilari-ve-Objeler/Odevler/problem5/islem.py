def hesapla():
    with open("sayilar.txt","r",encoding="utf-8") as file:
        kaynak=file.read()
        kaynak=kaynak.strip()
        kaynak=kaynak.replace(" ",",")
        kaynak=kaynak.split("\n")
        liste=list()
        for i in kaynak:
            i=i.split(",")
            liste.append(i)
        print(liste)


a=hesapla()
