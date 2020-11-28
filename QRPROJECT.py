import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img=cv2.imread('a.png')
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
with open('myDataFile.txt') as f:
    myDataList=f.read().splitlines()
#print(myDataList)
while True:
    success,img=cap.read()
    for barcode in decode(img):
        print(barcode.data)
        myData=barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput='Authorised'
            myColor=(0,255,0)
            #print('Authorised')
        else:
            myOutput = 'Un-Authorised'
            myColor = (0,0,255)
            #print('Un-Authorised')

        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2=barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)
    cv2.imshow('Result',img)
    cv2.waitKey(1)