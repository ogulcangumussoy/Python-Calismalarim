file=open("../Bilgiler.txt","r",encoding="utf-8")
liste= file.readlines() #bir diziye atar.
for i in liste:
    print(i,end="") #print'in kendi \n eklentisini kaldırdık.

file.close() #dosya kapatma gerekli
