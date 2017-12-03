import requests #Verileri çekeceğiz
from bs4 import BeautifulSoup #çekilen veri içerisinden bilgileri alacağız

url="https://yellowpages.com.tr/ara?q=Ankara"
response = requests.get(url) #response sayfa içerisindeki tüm verileri çektik

html_icerigi = response.content #html içeriği aldık

soup = BeautifulSoup(html_icerigi,"html.parser") #yazdırabilmek için beautifulsoup kütüphanesini kullandık
                                                # burda bu işlem için 'html.parser' kullanıldı.
#print(soup.prettify()) #içeriğin anlaşılır şekilde olması için prettify kullanıldı. Yazdırma işini yaptık.

#print(soup.find_all("a")) # find_all fonksiyonu a etiketlerinin bulunduğu bir liste döndürüyor.

# for i in soup.find_all("a"): #for döngüsü ile tek tek yazdırdık ve anlaşılır hale getirdik.
#     print(i.get("href"),"\n**************") #a'nın yanında href olması özelliğini de ekledik.
#     print(i.text)#tıklanınca yönlendirme yapan metinleri alırız.

print(soup.find_all("div",{"class":"yp-poi-box-2"})) #bu yapı ise find_all bir tık ilerisi ilk olarak div'e giriyor.
#ardından ,{} yapısı içerisine bir sözlük atıyoruz. eşleşmeye göre daha detaya inmiş oluyoruz.
