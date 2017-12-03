liste= list(range(15)) # 0 - 15 aralığında listemize eleman ekledik.
for i in liste:
    if (i==3 or i==5):
        continue  #nop diyebiliriz buraya geldiğinde boş geç i'yi bir arttır tekrar döngüye gir.
    print("i: ",i)
