import cv2
import numpy as np
import os

image_path = os.path.join(os.getcwd(),"opencv","images","chp2","nature.jpg")
image = cv2.imread(image_path)
cv2.imshow("image",image)
# bilateral
image_blt11= cv2.bilateralFilter(image,11,150,60)
cv2.imshow("image_blt7 ",image_blt11)
#mean
image_mn11=cv2.blur(image,(11,11))
cv2.imshow("image_mn7",image_mn11)
cv2.waitKey(0)