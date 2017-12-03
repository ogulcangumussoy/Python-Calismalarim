"""
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünelim
liste=["345","sadas","324a","14","kemal"]
bu listenin içindeki stringlerden içinde sadece rakam bulunduranları ekrana yazdırın try except bloklarını kullanmayı
unutmayın.
"""
liste= ["345","sadas","324a","14","kemal"]
for eleman in liste:
    try:
      eleman = int(eleman) #Eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak
      print(eleman)
    except:
        pass #pass deyimi bir blokun içerisinde hiçbir şey yapılmadığı anlamına geliyor.
            # Python'un hata vermemesi için kullanılır.


