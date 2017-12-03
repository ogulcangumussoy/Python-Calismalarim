"""
Bir dosya içerisindeki kayıtları göz önüne alarak harf hesaplaması yapacağız.
Burda kullanacağımız format :
Osman Aybar,50,20,100 şeklinde..  (1.sınav,ikinci sınav,final)
"""
def not_hesapla(satir):
    satir= satir[:-1] #-1' kadar ki olan yerleri al \n alınmayacak
    liste = satir.split(",") # '.'e göre ayırdık.
    isim= liste[0]
    not1= int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not= not1 *(3/10) +not2*(3/10)+not3*(4/10)
    if(son_not>=90):
        harf="AA"
    elif(son_not>=85):
        harf="BA"
    elif(son_not>=80):
        harf="BB"
    elif(son_not>=75):
        harf="CB"
    elif(son_not>=70):
        harf="CC"
    elif(son_not>=65):
        harf="DC"
    elif(son_not>=60):
        harf="DD"
    elif(son_not>=55):
        harf="FD"
    else:
        harf="FF"

    return isim + "---------------------->" +harf + "\n"

with open("futbolcular.txt","r",encoding="utf-8") as file: #sadece okuyacağız.
    eklenecekler_listesi = []
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("notlar.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)
