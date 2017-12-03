import smtplib #mail için gerekli kütüphane
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

"""
SMTP Modülü ile mail gönderme için ilk olarak az güvenli uygulamalar için öncelikle aşağıdaki linkten
engeli kaldırıyoruz.

https://myaccount.google.com/lessecureapps
"""

mesaj = MIMEMultipart()

mesaj["From"] = "kaynakMail@gmail.com"
mesaj["To"]= "hedefMail@gmail.com"
mesaj["Subject"]="Smtp2 Mail Gönderme"

yazi="""
Smtp ile Mail Gönderiyorum

Deneme Metni
"""

mesaj_govdesi= MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi) #mesaja ekledik mesaj gövdesini

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
