"""
Proje 2
Elinizde 5 kişinin maillerinin ve isimlerinin bulunduğu bir dosya olsun. Bu dosyayı okuyarak, her bir kişiye isimleriyle beraber mail göndermeye çalışın. Dosya formatı şu şekilde olacak.

                       Mustafa Murat Coşkun,coskun.m.murat@gmail.com
                                       //
                                       //
                                       //
                                       //
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

with open("mailler.txt","r",encoding="utf-8") as file:
    metin=file.read()
    liste=metin.split("\n")
    adlar=list()
    mailler=list()
    for i in liste:
        try:
            i=i.split(",")
            adlar.append(i[0])
            mailler.append(i[1])
        except:
            break

for ad,mail in zip(adlar,mailler):
    mesaj = MIMEMultipart()
    mesaj["From"] = "kaynakMail@gmail.com"
    mesaj["To"]= "{}".format(mail)
    mesaj["Subject"]="Smtp3 Mail Gönderme"
    yazi="""
    Try-Except
    Smtp ile Mail Gönderiyorum
    {}
    """.format(ad)
    mesaj_govdesi=MIMEText(yazi,"plain")
    mesaj.attach(mesaj_govdesi)

    #Gmail'e bağlanmamız gerekiyor

    try:
        mail=smtplib.SMTP("smtp.gmail.com",587)#Gmail smtp portuna bağlanmamız gerekiyor.
        mail.ehlo() #smtp serverina kendimizi tanıtıyoruz.
        mail.starttls() #mail'in şifrelenmesi için gerekiyor bu ikisi
        mail.login("mailAdresiniz@gmail.com","sifre") #mail serverına kullanıcı girişi yaptık
        mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string()) #mesaj içeriğine stringe çevirdik
        print("Mail Başarıyla gönderildi.")
        mail.close()  #SMTP Bağlantısını kestik
    except:#Herhangi bir hata olması durumu
        sys.stderr.write("Bir sorun oluştu!")
        sys.stderr.flush() #Bufferda yazılanı aniden yazdırmayı sağladık
