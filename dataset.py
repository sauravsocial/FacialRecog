import cv2
import numpy as np
import sqlite3
cam=cv2.VideoCapture(0)
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
def insertorUpdate(Id,Name):
    conn=sqlite3.connect("faceBase.db")
    cmd="SELECT * FROM people WHERE TeamID ="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE people SET AadharNumber="+str(Name)+ "WHERE TeamID="+str(Id)
    else:
        cmd="INSERT INTO people(TeamID,AadharNumber) Values("+str(Id)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id=raw_input('enter TeamID')
name=raw_input('enter AadharNo.')
insertorUpdate(id,name)
sampleNumber=0;

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNumber=sampleNumber+1
        cv2.imwrite("dataSet/User."+id+"."+str(sampleNumber)+".jpg",gray[y:y+w,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imshow("criminal",img)
    cv2.waitKey(100)
    if(sampleNumber>20):
        cam.release()
        cv2.destroyAllWindows()
        break



