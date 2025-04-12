import cv2 as cv
import numpy as np

img = cv.imread('photos/medium2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

# cv.imshow('sobelx',sobelx)
# cv.imshow('sobely',sobely)
cv.imshow('combined',combined_sobel)

canny=cv.Canny(gray,150,175)
cv.imshow('canny',canny)

cv.waitKey(0)
cv.destroyAllWindows()
