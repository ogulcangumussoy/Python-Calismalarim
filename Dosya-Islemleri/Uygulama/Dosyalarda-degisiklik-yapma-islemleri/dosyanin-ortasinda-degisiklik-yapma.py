with open("../Bilgiler.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Derslere Çalışılacak\n") #3.indise eleman ekledik
    file.seek(0) #dosyanın başına gittim
    #for i in liste: #tek tek yazma
     #   file.write(i)
    file.writelines(liste)
    file.seek(0)
    print(file.read())
