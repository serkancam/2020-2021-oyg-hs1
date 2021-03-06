import cv2
import numpy as np
import os

image_path = os.path.join(os.getcwd(),"opencv","images","chp2","salt-pepper.jpg")
image = cv2.imread(image_path)
cv2.imshow("image",image)

# median blur

image_b3 = cv2.medianBlur(image,3)
cv2.imshow("image_b3",image_b3)
image_b5 = cv2.medianBlur(image,5)
cv2.imshow("image_b5",image_b5)
image_b7 = cv2.medianBlur(image,7)
cv2.imshow("image_b7",image_b7)

cv2.waitKey(0)
