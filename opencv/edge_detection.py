import cv2
import os
import numpy as np

resim_yolu = os.path.join(os.getcwd(),"opencv","images","chp2","elma.jpg")
resim = cv2.imread(resim_yolu)
gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
cv2.imshow("gri",gri)
#blur

#sobelx
sobelx = cv2.Sobel(gri,cv2.CV_64F,1,0,ksize=3)
sobelx = np.uint8(np.absolute(sobelx))
cv2.imshow("sobelx",sobelx)
print(sobelx)
#sobely
sobely = cv2.Sobel(gri,cv2.CV_64F,0,1,ksize=3)
sobely= np.uint8(np.absolute(sobely))
cv2.imshow("sobely",sobely)
print(sobely)
# laplacian
laplace = cv2.Laplacian(gri,cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))
cv2.imshow("laplace",laplace)
print(laplace)
#canny 
canny = cv2.Canny(gri,50,170)
cv2.imshow("canny",canny)
cv2.waitKey(0)