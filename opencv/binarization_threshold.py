#binarization_threshold.py
import cv2
import numpy as np
import os

image_path = os.path.join(os.getcwd(),"opencv","images","chp2","scanned_doc.png")
image = cv2.imread(image_path)
print("image:",image.shape)
print(image[:10])
cv2.imshow("image",image)
# gray
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print("gray:",gray.shape)
cv2.imshow("gray",gray)
# binarization with threshold
(T,binarized_image) = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
print(binarized_image[-10:,-10:])
cv2.imshow("binarized_image",binarized_image)
# binarization with threshold inverse
(Ti,binarized_image_inv) = cv2.threshold(gray,60,255,cv2.THRESH_BINARY_INV)

cv2.imshow("binarized_image_inv",binarized_image_inv)
cv2.waitKey(0)