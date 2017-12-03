"""
1'den 10'a kadar olan sayılarla ekrana çarpım tablosu bastır.
"""
print("""
*******************************

ÇARPIM TABLOSU (1-10 ARASI)

*******************************
""")

for i in range(1,11):
    for j in range(1,11):
        print("{} x {} = {}\t".format(i,j,i*j))
    print("\n**********\n")
