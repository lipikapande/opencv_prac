import cv2 as cv

img = cv.imread('photos/paris.jpg')
cv.imshow('cat',img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#BGR TO HSV

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)

#BGR TO LAB
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)

#split
# b,g,r=cv.split(img)
# cv.imshow('blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)

# merged=cv.merge([b,g,r])
# cv.imshow('merge',merged)

#median blur
# median = cv.medianBlur(img, 3)
# cv.imshow('median',median)
# blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('Cat3',blur)

#bilateral blur - retains edges
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('blur',bilateral)

 
cv.waitKey(0)