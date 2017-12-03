from PIL import Image, ImageFilter  # Kütüphaneyi dahil ettik
image = Image.open("kus.jpg") #Resimi değişkenimize aldık
#image.save("kus2.jpg") #değişkendeki resmi başka bir isimle kaydettik
#image.show() #resmi ekrana bastık.
image.rotate(180).save("kus3.jpg") #Resmi döndürme işlemi yaptık.
image.convert(mode="L").save("kus3.jpg") #Siyah beyaz yapar
#***Boyut Değiştirme İşlemi
degistir = (960,600)
image.thumbnail(degistir)
image.save("kus6.jpg")
#******************
image.filter(ImageFilter.GaussianBlur(5)).save("kus7.jpg")#Blur verme işlemi 5 katsayı

#resim kırpma işlemi (x1,y1,x2,y2)

image2=Image.open("ataturk.jpg")
kirpilacak_alan=(340,0,950,600)
image2.crop(kirpilacak_alan).save("atam.jpg")
