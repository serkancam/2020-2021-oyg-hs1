#%% sınıf tanımlama

class IlkSinif:
    pass

o1 = IlkSinif()#__init__ methodu, yapıcı method
print(type(o1))
print(dir(IlkSinif))
print(20*"*",o1,20*"*",sep="\n")


# %% 
class Insan:
    def __init__(self,isim="yok",by=1.74,kl=78,sr="kahve"):#yapıcı method(constructor)
        self.ad=isim
        self.boy=by
        self.kilo=kl
        self.sacRengi=sr
        print("merhaba",self.ad)
    def __str__(self):
        return "adı:"+ self.ad + " boy:" + str(self.boy)
    
    # def __del__(self):#yıkıcı method(destructor)
    #     print("güle güle")


i1 = Insan()#init yapıcısı çalışır
i2 =Insan(isim="mehmet",sr="sarı")

print(i1.ad)
print(i2.ad)
print(i1)
print(i2)
# %% öğrenci
# public her yerden ulaşılır
# private sadece sınıf içerisinden ulaşılır. Türettiğin neseneden "." operatörü ile ulaşamazsın
class Ogrenci:
    def __init__(self,ad_,soyad_,okulNo_,notlar_:dict):
        self.ad=ad_.capitalize()
        self.soyad=soyad_.upper()
        self.okulNo=okulNo_
        self.__notlar=notlar_#private olur ve nesne tarfından ulaşıma kapatılır
    def ortalamaHesapla(self):
        ortalama=0
        ss=0
        for key in self.__notlar.keys():
            for nots in self.__notlar[key]:
                ss+=1
                ortalama+=nots

            # print(self.notlar[key])
        return ortalama/ss
    def getNot(self):
        return self.__notlar
    def NotEkle(self,dersKodu:str,notlar:list):
        for nt in notlar:
            if nt<=0:
                return -1
        
        self.__notlar[dersKodu]=notlar
        return len(notlar)
    

    

notlar_a={"mat9":[95,100,100],"fiz9":[100,100,90]}
notlar_y={"mat6":[100,95,100],"fen6":[95,95,90]}
arda = Ogrenci(ad_="arda",soyad_="hoşgör",okulNo_=130,notlar_=notlar_a)
yaman = Ogrenci(ad_="yaman",soyad_="karakuş",okulNo_=498,notlar_=notlar_y)


# arda.sacrengi="kumral"

# print(arda.sacrengi)

# yaman.ortalamaHesapla()
# arda.ortalamaHesapla()

# print(arda.getNot())
# arda.ortalamaHesapla()

print(yaman.NotEkle("sos6",[95,100]))
print(yaman.getNot())
# %% miras 

class Dizi(list):
    def toplam(self):
        toplam=0
        for s in self.copy():
            toplam+=s
        return toplam

dizi = Dizi()
dizi.append(10)
dizi.append(20)
dizi.append(30)
dizi.append(40)
dizi.append(50)
print(dizi.toplam())
# print(dizi.pop())

# print(dir(Dizi))

# %%
# Bir ısnıfta sdece public öğler miras yolu ile aktarılır
# miras alınansınıftaki bir method ezilebilir(override)
# Hiç miras almayan bir sınıf object sınıfını miras alır. Yani bütünn sınıflar object temel(base) sınıfını miras alır.
class Hayvan:
    def __init__(self,ad_):
        self.ad=ad_
        print("Hayvan init çalıştı.")
    def ses_cikar(self):
        print("Hayvan sınıfı ses çıkar")

class Kedi(Hayvan):
    def __init__(self):
        super()
        print("kedi init çalıştı")
    def ses_cikar(self):#method ezme(override)
       print("miyav...")
class Kopek(Hayvan):
    def ses_cikar(self):
        print("hav...")

h1=Hayvan("h1")
kd1=Kedi()
kp1=Kopek("karabaş")

kd1.ses_cikar()
h1.ses_cikar()
kp1.ses_cikar()
# %%
# çok biçimlilik 
def hayvanlar_ses_cikarsin(nesne):
    if isinstance(nesne,Hayvan):
        nesne.ses_cikar()

listem=[]
hayvanlar_ses_cikarsin(h1)    
hayvanlar_ses_cikarsin(kd1)    
hayvanlar_ses_cikarsin(kp1)    
hayvanlar_ses_cikarsin(listem)    
# %%
