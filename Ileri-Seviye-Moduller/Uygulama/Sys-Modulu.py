"""
Sys Modülü bizim sistemizde kurulu olan Python sürümünü yönettiğimiz standart bir modüldür. Bu modülü kullanarak
Python sistemine özgü fonksiyonları ve özellikleri kullanabiliriz.
"""
import sys
# print(dir(sys)) #sys içerisindeki fonksiyonları listeledik.
# #***********sys.exit kullanımı**********
# a= int(input("a:"))
# b=int(input("b:"))
# sys.exit()
# c=int(input("c:")) #bu komut sys.exit yüzünden çalışmaz.
# #*********sy.stderr ve stdout eklentileri

sys.stderr.write("Bu bir hata mesajıdır\n") #kirmizi renkte buffera yazdırdık
sys.stderr.flush() #Bunu kullanmazsak üstteki komutun hemen yazıldığını göremeyiz.
sys.stdout.write("Bu normal bir yazıdır\n")
