with open("../Bilgiler.txt","r+",encoding="utf-8")as file:
    icerik=file.read()
    icerik="Haftalık Program\n"+icerik #burda icerik değişkenimizi değiştirdik tekrardan dosyaya yazmak gerekiyor.
    file.seek(0)
    file.write(icerik)
    file.seek(0)
    print(file.read())

