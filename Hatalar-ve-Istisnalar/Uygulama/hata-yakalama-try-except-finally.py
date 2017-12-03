try:
    a = int(input("Sayi1: "))
    b=int(input("Sayi2: "))
    print(a / b)

except ValueError:
    print("Lütfen sayıda string kullanmayınız")
except ZeroDivisionError:
    print("Payda 0 olamaz.")
finally:
    print("Burası çalışmak zorunda")
print("İşlemler sonlandı.")
