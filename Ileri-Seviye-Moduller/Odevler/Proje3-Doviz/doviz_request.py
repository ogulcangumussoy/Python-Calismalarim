import requests
from bs4 import BeautifulSoup
import time


while True:
        url="http://www.doviz.com"
        response=requests.get(url)
        alinan_html=response.content
        soup=BeautifulSoup(alinan_html,"html.parser")

        html_icerik=soup.find_all('span', attrs={'class': 'menu-row2'})
        altin=html_icerik[0].text
        usd = html_icerik[1].text
        euro=html_icerik[2].text
        print("""
        *************************
        Döviz Değerleri Uygulaması
        *************************
        Altın: {}TL
        USD: {}TL
        EURO: {}TL
        """.format(altin,usd,euro))
        time.sleep(5)

