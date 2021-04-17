#%%
import numpy as np 
import pandas as pd 
from scipy import stats

veri=pd.read_csv("kalp_rahatsizligi.csv")
veri.head(3)

# %% 
print(veri.info())
# %% serum kolestrol değeri merkezi ölçütler
kol_ort=veri["serum_kolestrol"].mean()
kol_ortanca=veri.serum_kolestrol.median()
kol_mod=stats.mode(veri["serum_kolestrol"])
print("kolestrol ortlaması=",kol_ort)
print("kolestrol ortancası=",kol_ortanca)
print("kolestrol modu=",kol_mod)

# %% serum kolestrol dağılım ölçütleri
kol_min = veri["serum_kolestrol"].min()
kol_max =veri["serum_kolestrol"].max()
kol_aralik=kol_max-kol_min
kol_var=veri["serum_kolestrol"].var()
kol_std=veri["serum_kolestrol"].std()
print("kolestrol aralığı=",kol_aralik)
print("kolestrol varyansı=",kol_var)
print("kolestrol standart sapması=",kol_std)
# %% filtrleme kadınlar
veri_kadin=veri[veri["cinsiyet"]=="kadin"]
veri_kadin

# %% 40 yaşşındna büyük kadınlar
veri_kadin_40 = veri[(veri["cinsiyet"]=="kadin")&(veri.yas>40)]
veri_kadin_40

# %% kolestrolü ort-std ve ort+std arasında olanların sayısı
veri_cogunluk=veri[(veri.serum_kolestrol>=195)&(veri.serum_kolestrol<=298)]
print(len(veri_cogunluk))
# %% yas %68 yoğunluk
yas_ort= veri.yas.mean()
yas_std=veri.yas.std()
print(f"yaş verisinin yaklışık %68'i {yas_ort-yas_std} ile {yas_ort+yas_std} değerleri arasındaır.")
veri_sayısı=len(veri)

yas_yogunluk=veri[(veri.yas>=(yas_ort-yas_std))&(veri.yas<=(yas_ort+yas_std))]
yas_yogunluk_sayisi=len(yas_yogunluk)
print(f"verinin %68'i {veri_sayısı*0.68} dır. Ver standart sapmaya göre ise {yas_yogunluk_sayisi}")
# %%
