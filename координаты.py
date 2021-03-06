# Python-код для поиска координат
# контуры, обнаруженные на изображении.

import numpy as np
from tqdm import tqdm
import matplotlib as mpl
#лимит на кол-во точек на рисунке
mpl.rcParams['agg.path.chunksize'] = 10**10000
import matplotlib.pyplot as plt
import math

import cv2

image = cv2.imread("ris.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("edged.jpg", edged)
  
# Чтение изображения

font = cv2.FONT_HERSHEY_COMPLEX

img2 = cv2.imread('edged.jpg', cv2.IMREAD_COLOR)

  
# Чтение того же изображения в другом
# переменная и преобразование в серую шкалу.

img = cv2.imread('edged.jpg', cv2.IMREAD_GRAYSCALE)

  
# Преобразование изображения в двоичное изображение
# (только черно-белое изображение).

_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

  
#Обнаружение контуров в изображении.

contours, _= cv2.findContours(threshold, cv2.RETR_TREE,

                               cv2.CHAIN_APPROX_SIMPLE)

stri = []
# Проходя через все контуры, найденные на изображении.

for cnt in contours :

  

    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

  

    # рисует границу контуров.

    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5) 

  

    # Используется для выравнивания массива, содержащего

    # координаты вершин.

    n = approx.ravel() 

    i = 0

  

    for j in n :

        if(i % 2 == 0):

            x = n[i]

            y = n[i + 1]

  

            # Строка, содержащая координаты.

            string = str(x) + " " + str(y) 

            if(i == 0):

                # текст верхней координаты.

                cv2.putText(img2, "Arrow tip", (x, y),

                                font, 0.5, (255, 0, 0)) 

            else:

                # текст по оставшимся координатам.

                cv2.putText(img2, string, (x, y), 

                          font, 0.5, (0, 255, 0)) 
                stri.append([x, y])

        i = i + 1

  
# Отображение окончательного изображения.
print(stri)
cv2.imshow('image2', img2) 

fig, ax = plt.subplots()

for i in range(len(stri)):
    x = []
    y = []

    y.append(stri[i][1])
    y.append(stri[i][1]+0.001)

    x.append(stri[i][0])
    x.append(stri[i][0]+0.001)

    ax.plot(x, y, color = 'b', linewidth = 1)


#открывается окно, в котором вы можете увидеть диаграмму Вороного, построенную по данным вами координатами
plt.show()
  
# Выход из окна, если на клавиатуре нажата клавиша «q».

if cv2.waitKey(0) & 0xFF == ord('q'): 

    cv2.destroyAllWindows()