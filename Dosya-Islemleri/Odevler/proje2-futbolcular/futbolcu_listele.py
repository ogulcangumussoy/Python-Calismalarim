def futbolcu_listele(satir):
    satir= satir[:-1]
    liste=satir.split(",")
    ad=liste[0]
    takim=liste[1]

    if(takim=="Galatasaray"):
        with open("Galatasaray.txt","a",encoding="utf-8") as file1:
            yazdir= ad +"------>"+takim+"\n"
            file1.write(yazdir)
    elif(takim=="Fenerbahçe"):
        with open("Fenerbahce.txt","a",encoding="utf-8") as file1:
            yazdir= ad +"------>"+takim+"\n"
            file1.write(yazdir)
    elif(takim=="Beşiktaş"):
        with open("Besiktas.txt","a",encoding="utf-8") as file1:
            yazdir= ad +"------>"+takim+"\n"
            file1.write(yazdir)

with open("futbolcular.txt","r",encoding="utf-8") as file2:
    for i in file2:
        futbolcu_listele(i)
