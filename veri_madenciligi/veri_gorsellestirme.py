# %% kütüphaneler ve veri seti
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

veri = pd.read_csv("kalp_rahatsizligi.csv")
# print(veri.head(4))
veri.head(4)
# %%
veri.info()
# %% yaş histogramı
sns.histplot(data=veri, x="yas", bins=20)
plt.xlabel("yaş")
plt.ylabel("Adet")
plt.title("Yaş hverisi histogramı")
plt.xticks(np.arange(20, 90, step=10))
plt.show()

# %% yaş histogramı talasemiye göre
sns.histplot(data=veri, x="yas", hue="talasemi", element="step")
plt.xlabel("yaş")
plt.ylabel("Adet")
plt.title("Yaş verisi histogramı")
plt.show()

# %% yaş histogramını kalp rahatsızlığı sütununu ayırıcı olarak kullanıp grafik oluşturunuz.
sns.histplot(data=veri, x="yas", hue="kalp_rahatsizligi",
             element="step", palette="BuPu")
plt.xlabel("yaş")
plt.ylabel("Adet")
plt.title("Yaş verisi histogramı")
plt.show()
# %% saçılım grafiği:(scatterpolt)
# Saçılım diyagramı, iki farklı değişkenin arasındaki ilişkiyi belirlemek için kullanılır. Aralarındaki ilişkinin sebebi görülemese de, ilgili iki değişkenin arasında direkt olarak bir ilişki bulunup bulunmadığı ve bu ilişkinin ne derece güçlü olduğu görülebilir.
# %% kolestrol değeri ile en yüksek kalp hızı arasındaki saçılım grafiği
sns.scatterplot(data=veri, x="serum_kolestrol",
                y="en_yuksek_kalp_hizi", hue="cinsiyet")
plt.show()
# %% bu veriler arasındaki ilişkiyi göreceğiz
sns.regplot(data=veri, x="serum_kolestrol", y="en_yuksek_kalp_hizi")
plt.show()
# %%
sns.regplot(data=veri, x="yas", y="en_yuksek_kalp_hizi",)
plt.show()
# %% çizgi grafiği sayısal verilerin ilişkisini göstermek için veya genelde zamana bağlı depğişim için çizilir.
# yaş ve en yüksek kalp hızı ç.izgi grafiği

sns.lineplot(data=veri, x="yas", y="en_yuksek_kalp_hizi",
             hue="kalp_rahatsizligi")
plt.show()
# %% sütun/çubuk grafiği: kategorik verilerin görselleştirilmesinde sıklıkla kullanılır.

# cinsşyete göre kalp rahatsızlığın dağılımı
sns.countplot(data=veri, x="cinsiyet", hue="kalp_rahatsizligi")
plt.show()


# %% göğüs ağrısı tipinin kalp rahatsızlığına göre dağılımı
sns.countplot(data=veri, x="gogus_agrisi_tipi", hue="kalp_rahatsizligi")
plt.show()

# %%
sns.catplot(data=veri, x="gogus_agrisi_tipi",
            hue="kalp_rahatsizligi", col="aclik_kan_sekeri", kind="count")

plt.show()
# %%kutu garfiği:
# İstatistik biliminde kutu grafiği bir betimsel istatistik ve istatistiksel grafik aracı olup niceliksel veri görsel şekilde özetlemek için kutu-ve-bıyıklar grafiği adı altında bir açıklayıcı veri analizi aracı olarak geliştirilmiştir. (Kutu grafiği ile ilgili bilgi veri biliminde verilmiştir.)

sns.boxplot(data=veri, y="serum_kolestrol")
plt.show()
# %%
sns.boxplot(data=veri, y="serum_kolestrol", x="cinsiyet")
plt.show()
# %% serum kolestrol için üst ve alt sınır değerlerinin hesaplanması
veri.describe()
q1 = veri["serum_kolestrol"].describe()[4]
q3 = veri["serum_kolestrol"].describe()[6]
iqr = q3-q1
alt = q1-1.5*iqr
ust = q3+1.5*iqr
print(f"serum kolestrol alt sınırı:{alt}")
print(f"serum kolestrol ust sınırı:{ust}")


temiz = veri[(veri["serum_kolestrol"] >= alt) &
             (veri["serum_kolestrol"] <= ust)]

sns.boxplot(data=temiz, y="serum_kolestrol")
plt.show()

temiz


#%% ısı haritası grafiği:
# Isı haritası, sayısal özellikler/sütunlar arasındaki ilişkiyi görselleştirmek için kullanılan bir tekniktir.

veri.corr()
sns.heatmap(data=veri.corr(),annot=True,fmt="0.1f",linewidths=0.2)
plt.show()
# %%
