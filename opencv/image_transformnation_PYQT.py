import cv2
import numpy as np
import os
import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
import time

class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.ui_path=os.path.join(os.getcwd(),"opencv","animasyon.ui")
        self.kamera_durumu=False
        self.yuz_tanima_durumu=False
        self.InitUI()
    
    def InitUI(self):
        self.win=uic.loadUi(self.ui_path,self)
        #olaylar(event) bağlandı
        self.win.btnKameraAc.clicked.connect(self.kameraAcKapa)
        self.win.btnAnimation.clicked.connect(self.donen_zebra)
        self.win.btnYuzTanima.clicked.connect(self.yuz_tanima)
        self.win.show()
    def closeEvent(self,event):
        self.kamera_durumu=False
        self.yuz_tanima_durumu=False
    def yuz_tanima(self):
        #yüz bulma dosyası
        face_cascade_path=os.path.join(os.getcwd(),"opencv","haarcascade_frontalface_alt.xml")
        face_cascade =cv2.CascadeClassifier(face_cascade_path)
        self.yuz_tanima_durumu = not self.yuz_tanima_durumu
        self.win.lblCam.clear()
        cam = cv2.VideoCapture(0)     
        while self.yuz_tanima_durumu:
            ret,frame = cam.read()
            
            # yuz bulma 
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            # yuzler = face_cascade.detectMultiScale(gray,1.3,5)
            yuzler = face_cascade.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5,minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)
            for (x,y,w,h)in yuzler:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            # / yuz bıulma
            h,w,c=frame.shape
            step=c*w
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            qImg = QImage(frame.data, w, h,step, QImage.Format_RGB888)
            self.win.lblCam.setPixmap(QPixmap.fromImage(qImg))#rgb

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()


    def donen_zebra(self):
         # cam = cv2.VideoCapture(0)
        cd = os.getcwd()
        image_path = os.path.join(cd,"opencv","images","chp2","zebrasmall.png")

        image_original = cv2.imread(image_path) 
        h,w,c = image_original.shape
        angle = 0
        scale=1.0

      
        while True:

            rotation_matrix1 = cv2.getRotationMatrix2D((h//2,w//2),angle/360,scale)
            step=c*w
            frame = cv2.warpAffine(image_original,rotation_matrix1,(w,h))
            angle+=30

            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            qImg = QImage(frame.data, w, h,step, QImage.Format_RGB888)
            self.win.lblCam.setPixmap(QPixmap.fromImage(qImg))#rgb
          
            cv2.waitKey(0) # Tek hata wait key :)))

    def kameraAcKapa(self):
        self.kamera_durumu = not self.kamera_durumu
        self.win.lblCam.clear()        
        cam = cv2.VideoCapture(0)     
        while self.kamera_durumu:
            ret,frame = cam.read()#bgr
            
            h,w,c=frame.shape
            step=c*w
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            qImg = QImage(frame.data, w, h,step, QImage.Format_RGB888)
            self.win.lblCam.setPixmap(QPixmap.fromImage(qImg))#rgb            
            frame = cv2.GaussianBlur(frame,(7,7),0)
            cv2.imshow("Gaussian",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
            frame=cv2.medianBlur(frame,5)
            cv2.imshow("Median",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()
# # cd = os.getcwd()
# image_path = os.path.join(cd,"opencv","images","chp2","zebrasmall.png")

# image_original = cv2.imread(image_path) 
# h,w,c = image_original.shape

# center = (h//2,w//2)
# angle = 45
# scale = 1.0

# rotation_matrix1 = cv2.getRotationMatrix2D(center,angle,scale)
# rotation_matrix2 = cv2.getRotationMatrix2D((0,0),angle,scale)
# rotation_matrix3 = cv2.getRotationMatrix2D(center,angle,2.0)
# image_rotate1 = cv2.warpAffine(image_original,rotation_matrix1,(w,h))
# image_rotate2 = cv2.warpAffine(image_original,rotation_matrix2,(w,h))
# image_rotate3 = cv2.warpAffine(image_original,rotation_matrix3,(w,h))


# cv2.imshow("orijinal",image_original)
# time.sleep(0.5)
# cv2.imshow("orijinal",image_rotate1)
# time.sleep(0.5)
# cv2.imshow("orijinal",image_rotate2)
# time.sleep(0.5)
# cv2.imshow("orijinal",image_rotate3)
# cv2.waitKey(0)

if __name__=='__main__':
    app = QApplication(sys.argv)
    uygulama = App()
    sys.exit(app.exec_())


