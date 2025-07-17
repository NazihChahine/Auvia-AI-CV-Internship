import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('cat', img)

# Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade (Detect edges)
canny = cv.Canny(img , 125 , 127)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny , (7,7) , iterations=3)
cv.imshow('dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded' , eroded)

#Resize
resized = cv.resize(img , (500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized' , resized)

#Cropping
cropped = img[50:200 , 200:400]
cv.imshow('crop', cropped)

cv.waitKey(0) 