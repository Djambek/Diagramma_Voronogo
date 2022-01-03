#данная программа прекрасно ищет вершины на изображении с тонкими линиями 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
from matplotlib.pyplot import imshow
from PIL import Image, ImageFilter
import cv2

im1 = Image.open("lines.png")
img = im1.filter(ImageFilter.GaussianBlur(1))

img.save("img.png")

img = cv2.imread('img.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 16, 50, 50)

corners = cv2.goodFeaturesToTrack(blur, 40, 0.1, 10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.circle(img, (x, y), 3, 255, -1)
cv2.imwrite('img.png',img)

print(corners)
