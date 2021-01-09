#%%
sayi1 = 4454556445644556645465241454
sayi2= 524454454556445644556645465241454
print(sayi1*sayi2)
# %%
import numpy as np 

listem = [1,2,3]

nd1 = np.array(listem,dtype=np.uint8)

print(nd1.size)
print(nd1.shape)
print(nd1.dtype)
nd1[2]=260
print(nd1[2])
print(np.__version__)
print(type(nd1))
# %% boyutlara bakış
# 0-D skalar
import numpy as np
nd2 =np.array(38)
print(nd2.size)
print(nd2.shape)
print(nd2.shape)
print(nd2.dtype)
print(nd2.ndim)

# %% 1-D

nd3 = np.array([1,257,3],dtype=np.uint8)
print(nd3.size)
print(nd3.shape)
print(nd3.dtype)
print(nd3.ndim)
print(nd3[1])
# %% 2-D

nd4 = np.array([[1,2,3],[2,4,8]])
print(nd4.size)
print(nd4.shape)
print(nd4.dtype)

# %% 3-D
nd5= np.array([[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]]])
print(nd5.size)
print(nd5.shape)
print(nd5.dtype)
print(nd5.ndim)

# %% slice işlemleri

import numpy as np
#1-D slice
nd = np.arange(0,20,1)
# nd.dtype=np.uint8
print(nd)
print(nd[0])
print(nd[:3])
print(nd[-2:])
print(nd[10:-2])

#%%2- slice
nd6 = np.array([[1,2,3,10],[4,5,6,20],[7,8,9,30],[11,12,13,40]])
print(nd6.shape)
print(nd6)
print(nd6[0,])#[0]
print(30*"-")
print(nd6[1,])
print(30*"-")
print(nd6[:,3])#3. sütun
print(30*"-")
print(nd6[:,2])
print(30*"-")
print(nd6[2:,1:3])  #ikinci satırdan sonraki 
                    # satırların 1. ve 2. sütunları
print(30*"-")
print(nd6[0:2,2:])

#%% dizi oluşturma
# randint, arange
# zeros() ones() full() linspace()

import numpy as np

sifirlar = np.zeros((4,4),dtype=np.uint8)
print(sifirlar)

birler = np.ones((100,100),dtype=np.float32)
print(birler)

full8 = np.full((4,4,4),8)
print(full8)
#%%  linspace()

aralik = np.linspace(1,100,200,dtype=np.uint8)
print(aralik)
print(np.log2([2,4,8,16,1024,4096]))
#%%
#skaler işlemler
c=[3,4,5]
a = np.array([3,4,5],dtype=np.uint8)
b = np.array([7,10,20],dtype=np.uint8)
print(a+1)
print(30*"-")
print(a*11)
print(30*"-")
print(a/5)
print(30*"-")
print(a*a)
print(30*"-")
print(a**.5)
print(30*"-")
print(a+b)# shape eşitliği
print(30*"-")

# %% rastgele renklerden resim
import cv2
import numpy as np
image = np.random.randint(0,255,size=(300,300,3),dtype="uint8")

cv2.imshow("test",image)
cv2.waitKey(0)



# %%
import cv2,os
cd =  os.getcwd()
resim_yolu = os.path.join(cd,"numpy","bo2.png")
image = cv2.imread(resim_yolu)

cv2.imshow("resim",image)
cv2.waitKey(0)

# %%
