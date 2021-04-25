from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import os
import pandas as pd
import time

surucu_yolu = os.path.join(os.getcwd(),"veri_madenciligi","geckodriver.exe")
ayarlar = FirefoxOptions()
# ayarlar.add_argument("--headless")#tarayıcı grafik olarak gözükmüyor

surucu=webdriver.Firefox(options=ayarlar,executable_path=surucu_yolu)
surucu.get(url="https://www.dmo.gov.tr/Arama?k=%7c%7cElektronik%7c%7cBilgisayarlar%7c%7cDiz%c3%bcst%c3%bc+Bilgisayarlar&e=3")
time.sleep(3)
icerik = surucu.page_source
# print(icerik)
duzenli = BeautifulSoup(icerik,"html.parser")
a=[];f=[];adr=[];m=[];k=[]

urunler = duzenli.find_all(name="div",attrs={"class":"product-item"})
for urun in urunler:
    # print(urun)
    try:
        adi = urun.find(name="div",attrs={"class" :"title"}).text
        fiyat = urun.find(name="div",attrs={"class":"prices text-center"}).text
        adres= urun.find(name="div",attrs={"class" :"title"})
        adres = adres.find(name="a").get("href")
        marka_kod=urun.find(name="div",attrs={"class":"brand"}).text
        marka,kod=marka_kod.strip().split(" ")
        if adi and  fiyat:
            # print(f"{adi.strip()}--{fiyat.strip()}--{adres.strip()}")
            # print(marka_kod)
            a.append(adi)
            f.append(fiyat)
            adr.append(adres)
            m.append(marka)
            k.append(kod)
    except :
        print("ürün bilgi hatası")

veri = {"urun_adi":a,"urun_adresi":adr,"fiyat":f,"marka":m,"kod":k}
veri = pd.DataFrame(veri)
veri.to_csv("dmo_laptop.csv",index=False)