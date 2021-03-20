import os
import cv2
import numpy as np

cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","soccer-in-green.jpg")

image = cv2.imread(image_path)
h,w,c = image.shape
# translation matris
t_matris = np.float32([[1,0,-100],[0,1,-40]])

t_image = cv2.warpAffine(image,t_matris,(w,h))

cv2.imshow("orijinal",image)
cv2.imshow("t_imaj",t_image)

cv2.waitKey(0)
