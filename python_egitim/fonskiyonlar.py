# %% fonksiyonlar

# bir iş yapanlar
print("merhaba")

# sonuç döndürenler
a=input("sayı gir:")
print(input("giriş:"))
# %% ilk fonsiyon

# fonksiyon 2 kısımdan oluşur.
# tanım(definition) 
# çağırma-gerçekleme(call-invoke)

def ilkFonksiyon():
    print("merhaba dünya")

ilkFonksiyon()

# %% argüman veya parametre

def selam_ver(isim):
    print("merhaba",isim)

selam_ver("hasan")
ad="pınar"
selam_ver(ad)
selam_ver()

# %% birden fazla argüman kullanımı

def dortgen_alani(kk,uk):
    print("alan=",kk*uk)

dortgen_alani(20,30)
# %% örnek
# ad ve soyad argumanları
# alıp ekrana merhaba ad soyad
# merhaba hasan can

def selam_ver2(ad,soyad,yas):
    print("merhaba",ad,soyad,"yaş=",yas)

selam_ver2("hasan","can",13)

# bu argüman kullanımına konumsal yol 
# (positional way)
# %% anahtar kelime kullanımı (keywords way)
def selam_ver3(ad,soyad,yas):
    print("merhaba",ad,soyad,"yaş=",yas)

selam_ver3(yas=13,ad="hasan",soyad="can")

# %% karışık(mixing) paramtere kullanımı

def hesapla(a,b,c,d):
    sonuc = a+b*c/d
    print("sonuç=",sonuc,"|",a,b,c,d)

hesapla(1,2,10,2)#konuma bağlı
hesapla(a=10,d=8,b=20,c=3)#anahtar kelime yolu 
hesapla(1,5,d=3,c=10)#karışık kullanım
# karışık kullanımda
# ilk önce konuma bağlı argümanlar yazılır en son
# anahtar kelimeye bağlı argümanlar yazılır.
#hesapla(c=8,1,2,d=5)#hata
# hesapla(1,2,d=5,b=8) # hata
print("merhaba","nasılsın?",sep="½",end="@")
print()
print("merhaba","nasılsın?",end="½",sep="@")

# %% geriye değer döndürme return

def daire_alani(r):
    alan=3*r*r
    return alan#return 3*r*r

print("alan=",daire_alani(5))

# %% bir listeyi parametre olarak alıp liste
# elemanlarının toplamını bulsun ve 
# o sonucu gerei döndürsün
def liste_toplami(lst:list):
    t=0
    for eleman in lst:
        t+=eleman#t=t+eleman
    return t
    print("selam")

h=[1,2,30,52]
sonuc = liste_toplami(h)
print(sonuc)
# %% artık yıl mı?

# 00 ile biten yıllarda 400'e kalansız bölünenler
# bunun dışındaki yıllarda ise 4'e kalansız bölünenler
# artık yıldır
def artikYilMi(yil:int):#isLeapYear
    if yil%100==0 and yil%400==0:
        return True
    elif yil%4==0 and not(yil%100==0):
        return True
    else:
        return False

print(artikYilMi(2000))#True
print(artikYilMi(1700))#False
print(artikYilMi(2104))#True
print(artikYilMi(2001))#False
# %% asallık testi
def isPrime(sayi):
    for bolen in range(2,int(sayi**0.5)):
        if sayi%bolen==0:
            return False
    
    return True


isPrime(98765431)

# %% varsayılan değer deafault
def hacim(a, b=2, c=8):#hacim(a, b=2, c)
    return a*b*c


print(hacim(1, 5, 3))
print(hacim(1))
print(hacim(4, 6))
# soldan sağa varsayılan değer ,
# verilen argümandan sonra her argümana 
# varsayılan değer verilmelidir.

# %% varsayılan değer ve global
#
#
x=10

def bisey():
    print(x)

bisey()
print(x)
# %%

#

def bisey2():
    x=100
    print(x)

bisey2()
print(x)

# %%
x=222
def bisey2():
    # x=100
    print(id(x))

bisey2()
print(id(x))
# %% üçgen olur mu? && ||  !

def ucgenMi(a,b,c):
    return a+b>c and a+c>b and  b+c>a

print(ucgenMi(1,3,4))
print(ucgenMi(5,3,4))
print(ucgenMi(6,3,4))
print(ucgenMi(2,6,4))


# %% heron formülü

def ucgen_alani(a,b,c):
    if ucgenMi(a,b,c):
        s=(a+b+c)/2
        alan=(s*(s-a)*(s-b)*(s-c))**0.5
        return alan
    else:
        return "üçgen değil"



print(ucgen_alani(1,3,4))
print(ucgen_alani(3,4,5))
print(ucgen_alani(6,3,4))
print(ucgen_alani(2,6,4))
# %%  gauss formülü 1---n sayıların  toplamını

# 1. yol  formül
def gauss(n):
    return n*(n+1)/2

def ggauss(ilk,son):
    return gauss(son)-gauss(ilk-1)
print(gauss(5))
print(ggauss(3,999999999))




    
# %% 
# 2. yol iteratif
def iggauss(ilk,son):
    t=0
    for sayi in range(ilk,son+1):
        t+=sayi
    return

print(iggauss(3,999999999))

# %%c 1. yol fibonacci iteratif

def fib(n):
    if n<1:
        return None
    if n<3:
        return 1
    f1=1
    f2=1
    for _ in range(3,n+1):
        f1,f2=f2,f1+f2
    return f2

print(fib(10000))

# %% 3. özyinelemeli
# 3. özyineleme

def fibr(n):
    if n<1:
        return None
    if n<3:
        return 1
    return fibr(n-1)+fibr(n-2)
print(fibr(35))
# %% döngü olmadan döngü özyineleme

def geriSay(n):
    if n<1:
        return None
    print(n)
    geriSay(n-1)

def ileriSay(n):
    if n<1:
        return None
    
    ileriSay(n-1)
    print(n)
    

geriSay(4)
ileriSay(4)


# %%
