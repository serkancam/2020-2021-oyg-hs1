#%% sınıf tanımlama

class IlkSinif:
    pass

o1 = IlkSinif()
print(type(o1))


# %% 
class Insan:
    def __init__(self,isim="yok",by=1.74,kl=78,sr="kahve"):#yapıcı method(constructor)
        self.ad=isim
        self.boy=by
        self.kilo=kl
        self.sacRengi=sr
        print("merhaba",self.ad)
    def __str__(self):
        return self.ad+" bilgileri"
    
    # def __del__(self):#yıkıcı method(destructor)
    #     print("güle güle")


i1 = Insan()#init yapıcısı çalışır
i2 =Insan(isim="mehmet",sr="sarı")

print(i1.ad)
print(i2.ad)
print(i1)
print(i2)
# %%
