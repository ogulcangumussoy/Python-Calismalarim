#upper tüm harfleri büyüğe
#lower

print("python".upper())
print("PyThon".lower())

#replace metodu(stringdeki x değerini y ile değiştiriyor)
print("Herkes ana bacı gardaş".replace("a","o")) # a ve o değişti.
print("Python programlama Dili".replace(" ","-"))
print("Kunduz".replace("duz","zun"))#kalıplar da değiştirilebiliyor.

#startswith("x") x ile mi başlıyor.
#endswith("x") x ile mi bitiyor.

print("Python".startswith("Py"))
print("Python".endswith("gon"))

#split ile string parçalanıp listeye atılabilir.

liste="Python programlama dili".split(" ")
print(liste)
liste2="Python-Programlama-Dİli".split("-")
print(liste2)


#strip ile boşluk silme yapabiliriz. lstrip--> sol boşluk rstrip-->Sağ boşluk siler.

print("               Python            ".strip())
print("               Python            ".rstrip())
print(("<<<<<<<<<<<<<<<<<<<<<<<<Python2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>".rstrip(">").lstrip("<")))


#join metodu

liste=["21","02","2014"]
print("/".join(liste)) #seçtiğimiz bir şeyi dizinin parçalarına ekleyip toplu çıktı alabiliriz. 21/02/2014 gibi
liste2=["T","B","M","M"]
print(".".join(liste2))


#count(x) metodu seçilen şeyin metinde kaç kere geçtiğini döndürür.
#count(x,index) metodu index değerinden itibaren x kaç kere geçiyor diye bakar.

print("ada kapısı yandan çarklı".count("a"))
print("ada kapısı yandan çarklı".count("a",3))#3.indisten sonra bak.

#find(x) x değerini string içerisinde arar ilk bulduğu indisin nosunu verir.
#rfind(x) soldan bakıp ilk bulduğunu yazar eğer bulamazsa -1 döndürür ikisi de
print("araba".find("a"))
print("araba".rfind("b"))
print("araba".find("s")) #-1 döner
