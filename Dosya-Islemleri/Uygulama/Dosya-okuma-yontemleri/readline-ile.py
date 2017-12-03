"""
Readline tek satır okumaya yarar.
"""
file=open("../Bilgiler.txt","r",encoding="utf-8")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print("------------------------------")
print(file.readline()) #satır sayısı bitince boş döner
print(file.readline())
