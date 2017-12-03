"""
Program
1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. Daha sonra bir tane decorator
fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.

"""

def ekstra(fonk):

    def ekstra_ozellik():
        print("Mükemmel Sayılar...")
        for sayı in range(1,1001):
            toplam = 0
            i = 1
            while (i < sayı):
                if (sayı % i == 0):
                    toplam += i
                i +=1
            if (toplam == sayı):
                print(sayı)
        fonk()

    return ekstra_ozellik



@ekstra
def asal_sayilar():
    print("Asal Sayılar...")
    for sayı in range(2,1001):
        i = 2
        say = 0
        while (i < sayı):
            if (sayı % i == 0):
                say += 1
            i += 1
        if (say == 0):
            print(sayı)

asal_sayilar()
