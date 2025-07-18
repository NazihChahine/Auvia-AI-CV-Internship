import cv2 as cv

#changeResolution works only for live videos
def changeResolution(width , height):
    vid.set(3,width)
    vid.set(4,height)



#rescale works for everything
def rescale(frame,scale=0.5):
    height = int(frame.shape[0]*scale)
    width = int (frame.shape[1]*scale)
    dimensions= (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



vid = cv.VideoCapture(0)
while True:
    [isTrue, frame] = vid.read()
    cv.imshow('videoo',frame)
    

    if cv.waitKey(20) & 0xFF == ord('f'):
        break

vid.release()
cv.destroyAllWindows()

cv.waitKey(0)

