liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = list()

for i in liste: #Bunla [1,2,3] [4,5,6,7] şeklinde çıktılar gelir.
    for x in i:
       liste1.append(x)

print(liste1)
