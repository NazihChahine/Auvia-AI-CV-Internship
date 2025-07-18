import cv2 as cv 

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats' , img)


#Average Blur
average = cv.blur(img , (9,9))
cv.imshow('Average Blur',average)


#Gaussian Blur
gaussBlur = cv.GaussianBlur(img , (9,9),0)
cv.imshow('gauss' , gaussBlur)


#Median Blur
median = cv.medianBlur(img , 9 )
cv.imshow('Median Blur', median)


#Bilateral
bilateral = cv.bilateralFilter(img , 30, 30,30)
cv.imshow('bilateral' , bilateral)


cv.waitKey(0)