#%% kütüphanelerin aktarılması

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% dosyayı içe ataralım
veri = pd.read_csv("kalp_rahatsizligi.csv")
veri.head()
#sütun adlarını değiştireceğiz
#eksik veri içeren sütun ve satırlar nasıl silinir 
# eksik veriler nasıl giderilir.(ortalama, ortadanca, mod veya başka bir değer)
#sayısal değerleri normalize edeceğiz
#%% veriş seti bilgisi
print(veri.info())
# %%
veri.rename(columns={
    "gogus_agrisi_tipi":"gat",
    "hareketsiz_kan_basinci":"hkb",
    "serum_kolestrol":"sk",
    "aclik_kan_sekeri":"aks",
    "elektrokardiyografi":"ekg",
    "en_yuksek_kalp_hizi":"eykh",
    "anjin_bagli_egsersiz":"abe",
    "st_depresyonu":"st_d",
    "st_egimi":"st_e",
    "buyuk_damarlar":"bds"},inplace=True)

print(veri.info())
# %% bds ve talasemi sütununu çıakralım
veri2= veri.drop(["bds","talasemi"],axis=1)
print(veri2.info())
print(veri.info())

# %% kayıp veri oaln bütün satırları silelim
veri3=veri.dropna(axis=0)
print(veri3.info())

#%%
# bds değerinde ki kayıp veriler yerine en çok takrar eden verininin konulması
print(veri.info())
from sklearn.impute import SimpleImputer
imp_mod=SimpleImputer(missing_values=np.nan,strategy="most_frequent")
bds=veri["bds"].values.reshape(-1,1)
print(bds,"****")
bds_yeni = imp_mod.fit_transform(bds)
print(bds_yeni)
# %% kayıp verileri giderilen yapının yerine konması

print(veri.info())
veri["bds"]=bds_yeni
print("*"*30)
print(veri.info())

# %%
