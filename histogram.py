import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/medium2.jpg')
# cv.imshow('Dog',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Cat2',gray)

grey_hist = cv.calcHist([gray],[0],None, [256],[0,256])
plt.figure()
plt.title('Grayscale Hist')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(grey_hist)
plt.xlim([0,256])
plt.show()
 
plt.figure()
plt.title('COlor Hist')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b','g','r')
for i,col in enumerate(colors):
  hist = cv.calcHist([img],[i],None, [256],[0,256])
  plt.plot(hist,color=col)
  plt.xlim([0,256])


plt.show()

cv.waitKey(0)
cv.destroyAllWindows()