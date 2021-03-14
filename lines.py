import cv2 as cv
import numpy as np

img = cv.imread('paint.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

# Find the contour of the binary image
contours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[1:6]

cv.drawContours(img, cnt, -1, (0, 0, 255), 2)

cv.imshow('result',img)
cv.waitKey(0)
cv.destroyAllWindows()

"""# import the required library 
import numpy as np 
import cv2 
from matplotlib import pyplot as plt 


# read the image 
img = cv2.imread('paint.png') 

# convert image to gray scale image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# detect corners with the goodFeaturesToTrack function. 
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10) 
corners = np.int0(corners) 

# we iterate through each corner,  
# making a circle at each point that we think is a corner. 
for i in corners: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 3, 255, -1) 

plt.imshow(img), plt.show()"""
