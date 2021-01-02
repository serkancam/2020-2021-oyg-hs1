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

nd2 =np.array(38)
print(nd2.size)
print(nd2.shape)
print(nd2.dtype)

# %% 1-D

nd3 = np.array([1,300,3],dtype=np.uint8)
print(nd3.size)
print(nd3.shape)
print(nd3.dtype)
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

# %% slice işlemleri

nd6 = np.array([[1,2,3,10],[4,5,6,20],[7,8,9,30],[11,12,13,40]])
print(nd6.shape)
print(nd6[0,])
print(nd6[1,])
print(nd6[:,3])
print(nd6[:,2])
print(nd6[2:,1:3])
print(nd6[0:2,2:])

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
