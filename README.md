# Facial_Recognition-OpenCV_Python
Facial Recognition Project using Open Computer Vision (OpenCV) with Python

# Dependencies :-

Python 3x

OpenCV 3.1.0

SQlite

# Py libraries required

Numpy

PIL

cv2

# Working :-

# face_recog.py
All this Py does is,detects face (not recognise) and clicks a picture of the same (picture of face only,of certain dimension). Asks from new users for id and name. starts camera camera clicks 20 pictures and stores it as USER."userid".1.JPG , USER."userid".2.JPG upti USER."userid".20.jpg in (./dataset) And also Inserts id and name into sqlite database.

# face_recog1.py
All it does is trains a yml file to recognise the face from the taken dataset.

# face_recog2.py
This is the recogniser Starts the camera If picture is present in database,it recognizes the face(s) or else,dosen't
