import requests
import sys #en sonda hata mesajı bastırmak için dahil edildi.

url="http://api.fixer.io/latest?base=" #verileri çekeceğimiz site base=USD şeklinde kullanım olacak
#kullanıcı veri girişleri
birinci_doviz=input("Birinci Döviz:")
ikinci_doviz=input("İkinci Döviz:")
miktar=float(input("Miktarı Giriniz:"))

#istekte bulunduk. Burda response çıktısı seçtiğimiz para birimine göre yapılacak.
response=requests.get(url+birinci_doviz)#Bu işlem ile 'base='den sonraki alana seçilen değeri ekledik
json_verisi=response.json() #Aldığımız verileri json formatına çevirdik

try:#json içerisinde api'de tüm değerler çeviriliyor.Biz dizi mantığıyla içerisinde çevireceğimiz
    # para birimini seçtik ve Miktar ile çarptık.
    print(json_verisi["rates"][ikinci_doviz]*miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimini doğru giriniz.")#Kırmızı renkte içeriği bastık
    sys.stderr.flush() #Buffer'ı temizleyip hemen yazması için flush ettik.
