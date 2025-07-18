import cv2 as cv 

#img = cv.imread('photos/cat.jpg')
#cv.imshow('cat',img)


vid = cv.VideoCapture(0)
while True:
    [isTrue, frame] = vid.read()
    cv.imshow('videoo',frame)
    

    if cv.waitKey(20) & 0xFF == ord('f'):
        break

vid.release()
cv.destroyAllWindows()

cv.waitKey(0)

