import numpy as np
import cv2 as cv

haar_cacade = cv.CascadeClassifier('haar_face.xml')
people = ['Ben Afflek' , 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']


features = np.load('features.npy',allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\User\Desktop\opencv\Faces\val\ben_afflek\3.jpg')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)



faces_rect = haar_cacade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h , x:x+w]

    label,confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence : {confidence}')

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)

    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)