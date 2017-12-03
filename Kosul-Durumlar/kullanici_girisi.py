print("""****************************

Kullanıcı Girişi

****************************

""")

sys_kullanici_adi = "ogulcanGumussoy"
sys_parola="123456"

kullanici_adi = input("Kullanıcı Adınız: ")
parola = input("Parolanız: ")

if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("Parola Hatalı")
elif (kullanici_adi !=sys_kullanici_adi and parola == sys_parola):
    print("Kullanıcı Adı Hatalı")

elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print("Kullanıcı adı ve parola hatalı")
else:
    print("Giriş Yapıldı")
