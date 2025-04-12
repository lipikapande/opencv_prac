import os
import cv2 as cv
import numpy as np

p = []
for i in os.listdir(r'C:\Users\Lipika Pande\OneDrive\Desktop\New folder\opencv\photos\train'):
  p.append(i)
print(p)
dir1=r'C:\Users\Lipika Pande\OneDrive\Desktop\New folder\opencv\photos\train'
haar_cascade = cv.CascadeClassifier('haar_cascade.xml')

#our training set will consist of 2 lists
features=[] #image arrays of faces
labels=[]

def create_train():
  for person in p:
    path=os.path.join(dir1,person)
    label=p.index(person)

    for img in os.listdir(path):
      imgPath=os.path.join(path,img)
      imgArray=cv.imread(imgPath)
      gray=cv.cvtColor(imgArray,cv.COLOR_BGR2GRAY)
      faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
      
      for (x,y,w,h) in faces_rect:
        faces_roi=gray[y:y+h,x:x+w]
        features.append(faces_roi)
        labels.append(label)

create_train()
features=np.array(features,dtype='object')
labels=np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train the recognizer on the features and the labels list

face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)