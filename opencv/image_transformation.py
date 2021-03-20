import cv2
import numpy as np
import os

cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","zebrasmall.png")

image_original = cv2.imread(image_path) 
image_original = cv2.resize(image_original,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
h,w,c = image_original.shape

center = (h//2,w//2)
angle = 45
scale = 1.0
#
rotation_matrix1 = cv2.getRotationMatrix2D(center,angle,scale)
rotation_matrix2 = cv2.getRotationMatrix2D((0,0),angle,scale)
rotation_matrix3 = cv2.getRotationMatrix2D(center,angle,2.0)
image_rotate1 = cv2.warpAffine(image_original,rotation_matrix1,(w,h))
image_rotate2 = cv2.warpAffine(image_original,rotation_matrix2,(w,h))
image_rotate3 = cv2.warpAffine(image_original,rotation_matrix3,(w,h))

image_flip_horizatally = cv2.flip(image_original,1)
image_flip_vertically = cv2.flip(image_original,0)#-1 gelirse hem yatay hemde dikey aynalanmış olur

cv2.imshow("orijinal",image_original)
cv2.imshow("rotate1",image_rotate1)
cv2.imshow("rotate2",image_rotate2)
cv2.imshow("roate3",image_rotate3)
cv2.imshow("horizantal flip",image_flip_horizatally)
cv2.imshow("verticak flip",image_flip_vertically)
cv2.waitKey(0)


