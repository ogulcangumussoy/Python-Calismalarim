"""
Generator kullanarak fibonacci serisini yazdırmak
"""
def fibonacci():
    a=1
    b=1
    yield a #tek kullanımlık a yazıdırıldı.
    yield b #tek kullanımlık b yazıdırıldı.

    while True:
        a,b = b,a+b
        yield b

for sayi in fibonacci():
    if(sayi > 100000):
        break
    print(sayi)
