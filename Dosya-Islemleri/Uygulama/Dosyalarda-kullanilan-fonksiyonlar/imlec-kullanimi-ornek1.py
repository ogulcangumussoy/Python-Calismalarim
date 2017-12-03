with open("../Bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(5) #imleci 5'e çektik.
    icerik=file.read(10) #10 byte okuyacak.
    print(file.tell()) #imleç nerdeyse yazdır.
    print(icerik)
    file.seek(0) #imleci 0' çek
    icerik2=file.read(55) #55 byte oku
    print(icerik2,"\n",file.tell())


