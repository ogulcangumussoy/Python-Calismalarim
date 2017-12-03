try:
    file=open("../Bilgiler.txt","r",encoding="utf-8")
    icerik=file.read()
    print("Dosyanın İçeriği:\n",icerik)
    icerik2=file.read()
    print("Dostanın içeriği2\n",icerik2) #Bunun sonucu boş döner çünkü imleç önceki işlemden dolayı sonda

except FileNotFoundError:
    print("Dosya Bulunamadı....")
