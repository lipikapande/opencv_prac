import cv2 as cv

img = cv.imread('photos/medium2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv',thresh_inv)

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3)
cv.imshow('adaptive_thresh',adaptive_thresh)

cv.waitKey(0)