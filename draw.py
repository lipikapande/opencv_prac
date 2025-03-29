import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat1',img)
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('cats',img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# cv.imshow('Cat2',gray)
# blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('Cat3',blur)

# canny = cv.Canny(img,125,175)
# cv.imshow('Cat4',canny)

# dilated = cv.dilate(canny, (3,3),iterations=1)
# cv.imshow('Cat5',dilated)

# eroded = cv.erode(dilated,(3,3),iterations=1)
# cv.imshow('Cat6',eroded)

# resized = cv.resize(img,(500,500))
# cv.imshow('Cat3',resized)

# cropped = img[50:200,200:400]
# cv.imshow('Cat4',cropped)

# # blank[200:300, 300:400] = 0,255,0
# # cv.imshow('green',blank)
# # cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
# # cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# # cv.imshow("rec",blank)
# cv.putText(blank, "H",(blank.shape[1]//2, blank.shape[0]//2),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
# cv.imshow("rec",blank)

# def translate(img,x,y):
#   transMat = np.float32([[1,0,x],[0,1,y]])
#   dimensions = (img.shape[1],img.shape[0])
#   return cv.warpAffine(img,transMat,dimensions)

# translated = translate(img,30,30)
# cv.imshow('translated',translated)

# def rotate(img,angle,rotPoint=None):
#   (height,width)=(img.shape[1],img.shape[0])
#   if rotPoint is None:
#     rotPoint=(width//2,height//2)
#   rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
#   dimensions = (width,height)
#   return cv.warpAffine(img,rotMat,dimensions)

# rotated = rotate(img,45)
# cv.imshow('rotated',rotated)

# flip=cv.flip(img,1)
# cv.imshow('flipped',flip)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny = cv.Canny(img,125,175)
cv.imshow('Cat4',canny)

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found: ')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contours_drawn',blank)

cv.waitKey(0)
cv.destroyAllWindows()
