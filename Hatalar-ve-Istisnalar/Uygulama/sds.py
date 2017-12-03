def çift_mi(sayı):

    if (sayı % 2 == 0):
        return sayı
    else:
        raise ValueError("hata basdık")
liste = [34,2,1,3,33,100,61,1800]

for i in liste:
    try:
        print(çift_mi(i))
    except ValueError:
        pass
