#Listemizdeki değerlerden çift olanlarını yazdırdık.


liste = [1,2,3,4,5,6,7,15,19,22,29,37,48]

for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)
