def tambolenler(sayi):
    for i in range(1,sayi+1):
        if(sayi%i==0):
            listemiz.append(i)
    return listemiz

while True:
    sayi=input("Sayiyi giriniz: ")
    if(sayi=="q"):
        print("Program sonlandırılıyor.")
        break
    else:
        sayi=int(sayi)
        listemiz=list()
        liste=tambolenler(sayi)
        print("Tam Bölenler: ",liste)
