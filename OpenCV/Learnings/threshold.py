import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)


#Simple thresholding
threshold , thresh = cv.threshold(gray , 150,255,cv.THRESH_BINARY)
cv.imshow('simple Thresholded', thresh)


threshold , thresh_inv = cv.threshold(gray , 150,255,cv.THRESH_BINARY_INV)
cv.imshow('simple Thresholded Inverse', thresh_inv)


#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)





cv.waitKey(0)
