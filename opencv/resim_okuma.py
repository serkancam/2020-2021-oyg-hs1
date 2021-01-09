import cv2
import os

cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","road.jpg")
# print("bulunulan dizin:",cd)
image = cv2.imread(image_path)
#resim boyut bilgileri
shape = image.shape
print(type(image))
print(shape)
w=shape[1]
h=shape[0]
print(f"resim boyutu {w}x{h}")
#ilk piksel rengi

ilk_renk = image[0,0]
print(ilk_renk)

# ilk 100x100 piksel ilk piksel rengine dönüşsün
image[0:100,0:100]=ilk_renk

#çizgi çizme
start = (w//2,h//2)
end = (w,h)
renk = (0,0,255)
renk2=(255,0,0)
thickness=5
cv2.line(image,start,end,renk,thickness)
cv2.rectangle(image,start,end,renk2,thickness)


cv2.imshow("resim",image)#image[::2,::2]

cv2.waitKey(0)