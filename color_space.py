import cv2 as cv

img = cv.imread('photos/paris.jpg')
cv.imshow('cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#BGR TO HSV

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)

#BGR TO LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)

#split
b,g,r=cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

merged=cv.merge([b,g,r])
cv.imshow('merge',merged)
 
cv.waitKey(0)