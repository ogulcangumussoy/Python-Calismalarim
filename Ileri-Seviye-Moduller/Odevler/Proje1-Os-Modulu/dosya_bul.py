import os
sayac=1
sayac2=1
sayac3=1
for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("/home/ogulcan/Desktop"):

    for i in dosya_isimleri:
        if(i.endswith(".pdf")):

            with open("PDF-Dosyalari.txt","a",encoding="utf-8") as file:
                if(sayac==1):
                    file.write("Tüm PDF Dosyaları\n\n")
                    sayac+=1
                else:
                    yazdir= "Dosyanın Adı:"+i+"\nBulunduğu Dizin:"+klasor_yolu+"\n*******************\n"
                    file.write(yazdir)

        elif(i.endswith(".mp4")):

            with open("MP4-Dosyalari.txt","a",encoding="utf-8") as file:
                if(sayac2==1):
                    file.write("Tüm Mp4 Dosyalar\n\n")
                    sayac2+=1
                else:
                    yazdir= "Dosyanın Adı:"+i+"\nBulunduğu Dizin:"+klasor_yolu+"\n*******************\n"
                    file.write(yazdir)

        elif(i.endswith(".mp4")):

            with open("MP4-Dosyalari.txt","a",encoding="utf-8") as file:
                if(sayac2==1):
                    file.write("Tüm Mp4 Dosyalar\n\n")
                    sayac2+=1
                else:
                    yazdir= "Dosyanın Adı:"+i+"\nBulunduğu Dizin:"+klasor_yolu+"\n*******************\n"
                    file.write(yazdir)

        elif(i.endswith(".txt")):

            with open("TXT-Dosyalari.txt","a",encoding="utf-8") as file:
                if(sayac3==1):
                    file.write("Tüm TXT Dosyalar\n\n")
                    sayac3+=1
                else:
                    yazdir= "Dosyanın Adı:"+i+"\nBulunduğu Dizin:"+klasor_yolu+"\n*******************\n"
                    file.write(yazdir)
