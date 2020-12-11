# %% iki boyutlu listeler

ll=[[1,2,3],[4,5,6],[7,8,9,4]]

print(ll[1][1])

for el1 in ll:
    for el2 in el1:
        print(el2,end=" ")
    print()
# %% dir komutu

listem=[1,2,3]
listem.clear()

#print(dir(listem))
# appdend liste sonuna eleman ekler
print(listem)
listem.append(10)
print(listem)
listem.append(20)
print(listem)
listem.append(30)
print(listem)
#insert istenilen indexe eleman ekler
listem.insert(1,4)
print(listem)
print(listem[2])
# acaba ben hep eklenen değeri lisenin başına 
# nasıl eklerim
print(listem)
listem.insert(-1,222)
print(listem)
listem.insert(0,333)
print(listem)
listem.insert(0,444)
print(listem)

# %% pop komutu 
# listenin sonundaki elemanı döndürür
# ve siler
liste=[444, 333, 10, 4, 20, 222, 30]
print(liste.pop())
print(liste)

for _ in range(3):
    print(liste.pop(0))
    print(liste)
# %%
isim="abracadabra"
print(isim[::2])
# %%  

print(dir(list))

# %% clear tüm elemanları siler

listem=[i for i in range(10)]
print(listem)
listem=[0 for i in range(10)]
print(listem)
listem=[i**3 for i in range(10)]
print(listem)
listem.clear()
print(listem)

# %% remove
listem=[i**3 for i in range(10)]
listem.append(0)
print(listem)
listem.remove(0)
print(listem)
del listem[5]
print(listem)
print(listem.remove(27))
print(listem.remove(27))
# %%
listem=[27 for i in range(5)]
l2=[72,38,58,27,27,27]
listem=listem+l2
print(listem)
silinecek=27
say=0
for i in listem:
    say+=1
    if(i==silinecek):
        listem.remove(i)
# for i in range(len(listem)):
#     if(listem[i]==silinecek):
#         del listem[i]
#         listem.insert(i,-1)
# print(listem,"\nsay=",say)

# while silinecek in listem:
#     listem.remove(silinecek)

print(listem)
# %% count bir listede bir elamandan kaç tane var
a=[27,27,27]
l=[27, 27, 27, 27, 27, 72, 38, 58, [27, 27, 27]]
print(l.count(27))
print(l.count(a))
print(l.count([27,27,27]))
print(l.count(2))



# %%  copy değerleri koplayalar
a=5
b=a
a=10
print(a,b)


l1=[1,2,3]
# l2=l1
l2=l1.copy()
l1.append(333)
print(l1,l2,sep="@")


# %% sort reverse

import random
# l3=[]

# for _ in range(10):
#     l3.append(random.randint(1,1000))

print(l3)
l3.sort()
print(l3)
l3.reverse()
print(l3)
# %% str
isim=""
print(dir(str))
print(dir(isim))

# %%
