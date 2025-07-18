import cv2 as cv 
import numpy as np

#BLANK
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank', blank)

#COLOR
blank[:] = 0,255,0
cv.imshow('green',blank)

#RECTANGLE
cv.rectangle(blank, (0,0) , (blank.shape[1]//2, blank.shape[0]//2), (0,255,0),thickness=2)
cv.imshow('rectangle', blank)

#CIRCLE
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
cv.imshow('circle', blank)

#LINE
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('line', blank)

#TEXT
cv.putText(blank,'Helloo',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),2)
cv.imshow('Text', blank)







cv.waitKey(0)