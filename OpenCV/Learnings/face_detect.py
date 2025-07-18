import cv2 as cv

img = cv.imread('photos/group 1.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayPerson',gray)

haar_cacade = cv.CascadeClassifier('haar_face.xml')


faces_rect = haar_cacade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2)

print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces' , img)

cv.waitKey(0)