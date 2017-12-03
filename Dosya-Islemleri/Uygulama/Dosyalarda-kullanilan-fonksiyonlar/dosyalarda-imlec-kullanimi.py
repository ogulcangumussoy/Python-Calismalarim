try:
    with open("../Bilgiler.txt","r",encoding="utf-8") as file:
        print(file.tell()) #dosya imlecinin nerde olduğunu döndürür.
        file.seek(20) #imleci 20 ilerlettik.(20.byte)
        print(file.tell())
except FileNotFoundError:
    print("Dosya Bulunamadı..")
