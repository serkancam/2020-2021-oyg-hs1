import os 
import cv2
import numpy as np 
yol = os.path.join(os.getcwd(),"opencv","images","chp2","rice-bw-2.png")
resim = cv2.imread(yol)# boyut 3 tür, channel (B,G,R)
print(resim.shape)
gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
print(gri.shape)
t,sbResim = cv2.threshold(gri,110,255,cv2.THRESH_BINARY)
# cv2.imshow("resim",resim)
cv2.imshow("sbResim",sbResim)
# kontur bulma
konturlar,_=cv2.findContours(sbResim,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(konturlar),type(konturlar))
print(konturlar[0][0][0])
xy1=konturlar[0][0][0]
xy2=konturlar[0][1][0]
xy3=konturlar[0][2][0]
xy4=konturlar[0][3][0]
cv2.circle(resim,tuple(xy1),5,(0,0,255),-1)
cv2.circle(resim,tuple(xy2),5,(0,0,255),-1)
cv2.circle(resim,tuple(xy3),5,(0,0,255),-1)
cv2.circle(resim,tuple(xy4),5,(0,0,255),-1)
cv2.imshow("resim konturlar",resim)
# konturları çizdir
for kontur in konturlar:
    deger = cv2.approxPolyDP(kontur,0.009*cv2.arcLength(kontur,True),True)
    cv2.drawContours(resim,[deger],0,(0,255,0),2)
cv2.imshow("resim konturlar",resim)
cv2.waitKey(0)
