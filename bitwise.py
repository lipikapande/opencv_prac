import cv2 as cv
import numpy as np

# img = cv.imread('photos/cat.jpg')
# cv.imshow('Cat1',img)
blank = np.zeros((400,400),dtype='uint8')
cv.imshow('blank',blank)

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('rec',rectangle)
cv.imshow('circle',circle)

bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)

#bitwise and, or, xor

cv.waitKey(0)