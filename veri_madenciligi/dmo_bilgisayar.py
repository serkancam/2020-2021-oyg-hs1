# import requests
# from bs4 import BeautifulSoup
# site = requests.get("https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98")

# kaynak = BeautifulSoup(site.content,"lxml")
# print(kaynak)
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import os
import pandas as pd
import time

yol = os.path.join(os.getcwd(), "veri_madenciligi", "geckodriver.exe")
dosya_yolu=os.path.join(os.getcwd(), "veri_madenciligi", "dmo.csv")
options = FirefoxOptions()
# options.add_argument("--headless") 
driver = webdriver.Firefox(options=options, executable_path=yol)
driver.get("https://www.dmo.gov.tr/Arama?s=&k=%7c%7cElektronik%7c%7cBilgisayarlar%7c%7cDiz%c3%bcst%c3%bc+Bilgisayarlar&p=1&d=SM&e=1")
content = driver.page_source
soup = BeautifulSoup(content, "lxml")
print(soup)