def ekstra(fonk): #fonk ortalamabul anlamina geliyor.
    def wrapper(sayilar): #ortalamabul içerisine gelen sayilar dizisi decorator içerisine otomatik olarak gelir.
        ciftler_toplami=0
        cift_sayilar=0
        tekler_toplami=0
        tek_sayilar=0
        for sayi in sayilar:
            if(sayi % 2 == 0):
                ciftler_toplami+=sayi
                cift_sayilar+=1
            else:
                tekler_toplami+=sayi
                tek_sayilar+=1
        print("Teklerin Ortalaması:",tekler_toplami/tek_sayilar)
        print("Çiftlerin Ortalaması:",ciftler_toplami/cift_sayilar)
        fonk(sayilar) #Ekstralar ardından ortalamabul(sayilar)'i calıstırdık
    return wrapper

@ekstra #decorator tanımlaması yapıldı.
def ortalamabul(sayilar):
    toplam = 0

    for sayi in sayilar:
        toplam+=sayi
    print("Genel Ortalama:",toplam/len(sayilar))

ortalamabul([1,2,3,34,60,63,32,100,105])
