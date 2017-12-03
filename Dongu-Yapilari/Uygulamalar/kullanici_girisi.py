print("""
********************************

Kullanıcı Giriş Programı

********************************
""")

sys_kullanici_adi ="ogulcan"
sys_parola = "12345"
giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı:")
    parola= input("Parola: ")
    if(kullanici_adi !=sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakki -=1
    elif(kullanici_adi==sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatalı....")
    elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı adı ve Parola Hatalı")
        giris_hakki -=1
    else:
        print("Sisteme başarıyla giriş yapıldı...")
        break

    if(giris_hakki == 0):
        print("Giriş Hakkınız Bitti")
        break
