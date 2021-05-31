
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

URL = "https://www.instagram.com/"

def verileri_al(kullanici_adi):
    son_url = URL + kullanici_adi

    request = Request(son_url, headers={'User-Agent':'Mozilla/5.0'})
    html_verisi = urlopen(request).read()

    soup = BeautifulSoup(html_verisi, 'html.parser')

    veri = soup.find("meta",property="og:description").attrs['content']

    veri = veri.split("-")[0]

    veri = veri.split(" ")

    print("takipci sayisi: "+veri[0])
    print("takip edilen sayisi: "+veri[2])
    print("gonderi sayisi: "+veri[4])


kullanici_adi = input("kullanici adi giriniz: ")
verileri_al(kullanici_adi)

