import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('cat' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
cv.waitKey(0)