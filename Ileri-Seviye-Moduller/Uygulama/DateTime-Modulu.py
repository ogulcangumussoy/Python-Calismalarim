from datetime import datetime #datetime modülü içerisinden datetime sınıfını dahil ettik
import locale

locale.setlocale(locale.LC_ALL,"") #Dili türkçe yapar
print(datetime.now()) #anlık zaman basar
su_an= datetime.now()
print(su_an.year) #yılı basar
print(su_an.month) #ayı basar
print(su_an.hour)#saati basar

print(datetime.ctime(su_an)) #Daha anlaşılır bir çıktı verir. Mon November tarzı
print("-----------------")
print(datetime.strftime(su_an,"%Y")) #Sadece yılı basar 2017
print(datetime.strftime(su_an,"%B")) #Ay basar November
print(datetime.strftime(su_an,"%A")) #Gün ismi Monday
print(datetime.strftime(su_an,"%X")) #Saat basar 23:00:14
print(datetime.strftime(su_an,"%D")) #Gün bilgisi 11/27/17

print(datetime.strftime(su_an,"%Y %B %A")) #2017 November Monday

saniye =datetime.timestamp(su_an) #saniye hesaplar datetime objesini saniyeye çevirir.
print(saniye)
su_an2 = datetime.fromtimestamp(saniye) #saniye türünden geleni datetime'a çevirir.
print(su_an2)

su_an=datetime.fromtimestamp(0) #Milat değerini verir 1970 epoch time
print(su_an)

tarih = datetime(2017,7,12)
su_an=datetime.now()
olcu=su_an-tarih
print(datetime.timestamp(tarih))
