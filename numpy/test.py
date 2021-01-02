import cv2,os
cd =  os.getcwd()
resim_yolu = os.path.join(cd,"numpy","bo2.png")
image = cv2.imread(resim_yolu)
image_cut = image[0:250,600:800,:]
cv2.imshow("resim",image_cut)
cv2.waitKey(0)
