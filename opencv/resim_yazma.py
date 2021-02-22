import cv2
import os
import numpy as np 
#300x300 px lik bir siyay resim
canvas_r = np.zeros((300,300,3),dtype=np.uint8)
canvas_c=canvas_r.copy()
# dörtgen parametreleri
start = (100,100)
end= (200,200)
color_r = (0,0,255)
thickness_r=4
# dörtgeni çizdik
cv2.rectangle(canvas_r,start,end,color_r,thickness_r)
#çember çizdik
center = (150,150)
radius = 75
color_c = (255,0,0)
thickness_c=-1#-1 içi dolu bir geometrik şekil
cv2.circle(canvas_c,center,radius,color_c,thickness_c)
# şekli ekranda gösterdik
cv2.imshow("Rectangle",canvas_r)
cv2.imshow("Circle",canvas_c)
# rectangle kayıt edelim
cd = os.getcwd()
image_path_r = os.path.join(cd,"opencv","images","chp1","rectangle.jpg")
cv2.imwrite(image_path_r,canvas_r)
# circle kaydedelim
image_path_c = os.path.join(cd,"opencv","images","chp1","circle.jpg")
cv2.imwrite(image_path_c,canvas_c)
cv2.waitKey(0)