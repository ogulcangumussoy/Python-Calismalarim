def anafonksiyon(islem_adi):

    def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpim(*args):
        carpim=1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplama
    else:
        return carpim

fonk= anafonksiyon("toplama") #bunun sayesinde return toplamaya girdik ordanda iceriği toplama fonksiyonuna ilettik
print(fonk(1,2,3,4,5,6,7))
fonk2=anafonksiyon("carpim") #normal şarttan iç fonksiyona giremeyiz ama böyle olunca carpim fonksiyonuna yönlendik
print(fonk2(1,2,3,4,5))
