import cv2
import numpy as np 
import time

cap = cv2.VideoCapture(-1)# unix te ilk capture cihazı -1 windows ta 0 olarak işaretlenir

ret1,frame1=cap.read()
ret2,frame2=cap.read()
while cap.isOpened():
    #hareket tespit
    fark = cv2.absdiff(frame1,frame2)
    gri =cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    yumusak = cv2.GaussianBlur(gri,(5,5),0)
    t,sbResim=cv2.threshold(yumusak,20,255,cv2.THRESH_BINARY)
    yayilmis = cv2.dilate(sbResim,None,iterations=3)
    konturlar,hiyerarsi= cv2.findContours(yayilmis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # print(len(konturlar)
    # print(konturlar)
    for kontur in konturlar:
        (x,y,w,h)=cv2.boundingRect(kontur)
        if cv2.contourArea(kontur)<1800:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"hareket algilandi",(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)


    
    #gösterimler
    cv2.imshow("frame1",frame1)
    # cv2.imshow("fark",fark)
    # cv2.imshow("fark-gri",gri)
    # cv2.imshow("fark-gri-blur",yumusak)
    # cv2.imshow("fark-gri-blur-binarization",sbResim)
    cv2.imshow("fark-gri-blur-binarization-dilate",yayilmis)
    frame1=frame2
    # time.sleep(0.4)
    ret2,frame2=cap.read()
    if cv2.waitKey(40)==27:# escape tuşunun ascii değeri 27 dir
        break

cv2.destroyAllWindows()
cap.release()