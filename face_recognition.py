import numpy as np
import cv2 as cv

haar_cascade=cv.CascadeClassifier('haar_face.xml')

# features=np.load('features.npy')
# labels=np.load('labels.npy')
haar_cascade = cv.CascadeClassifier('haar_cascade.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

p=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

img=cv.imread(r'C:\Users\Lipika Pande\OneDrive\Desktop\New folder\opencv\photos\val\ben_afflek\2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces_rect:
  faces_roi=gray[y:y+h,x:x+h]
  label, confidence = face_recognizer.predict(faces_roi)
  print(f'Label = {p[label]} with a confidence of {confidence}')
  cv.putText(img,str(p[label]),(20,20),cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0),thickness=2)
  cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected face', img)
cv.waitKey(0)