import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
cv.imshow('original' , img)

#Translation
def translate(img , x, y) : 
    transMAT = np.float32([[1,0,x],
                           [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMAT,dimensions)

# -x --> left
# -y --> Up
# x --> Right
# y --> Down
    
tranlated  = translate ( img , -100 , 100)
cv.imshow('Translated' , tranlated)


#Rotation 
def rotate(img , angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None : 
        rotPoint = (width//2 , height //2)

    rotMAT = cv.getRotationMatrix2D(rotPoint , angle,1.0 )
    dimensions = (width, height)

    return cv.warpAffine(img , rotMAT,dimensions)

rotated = rotate(img , 45)
cv.imshow('rotated', rotated)

#Cropped
cropped = img[200:400 , 300 : 400]
cv.imshow('Cropped' , cropped)

cv.waitKey(0)