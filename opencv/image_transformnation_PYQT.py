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
        self.InitUI()
    
    def InitUI(self):
        self.win=uic.loadUi(self.ui_path,self)
        self.win.btnKameraAc.clicked.connect(self.kameraAcKapa)
        self.win.btnAnimation.clicked.connect(self.donen_zebra)
        self.win.show()
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
        cam = cv2.VideoCapture(0)
     
        while True:
            ret,frame = cam.read()#bgr
            h,w,c=frame.shape
            step=c*w
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            qImg = QImage(frame.data, w, h,step, QImage.Format_RGB888)
            self.win.lblCam.setPixmap(QPixmap.fromImage(qImg))#rgb

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
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


