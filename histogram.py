import cv2 as cv

img = cv.imread('photos/medium2.jpg')
cv.imshow('Dog',img)

cv.waitKey(0)