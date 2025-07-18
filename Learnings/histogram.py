import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/cats.jpg')
cv.imshow('cats',img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray' , gray )


# #GrayScale Histogram
# gray_histo = cv.calcHist([gray],[0],None,[256],[0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_histo)
# plt.xlim([0,256])
# plt.show()


plt.figure()
plt.title('color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')


#color histogram
colors = ('b' , 'g' , 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img] , [i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
