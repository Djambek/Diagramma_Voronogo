import numpy as np
from tqdm import tqdm
import matplotlib as mpl
#лимит на кол-во точек на рисунке
mpl.rcParams['agg.path.chunksize'] = 10**10000
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

#кол-во садовников
num_of_gardeners = 1

#координаты х и у на графике.В них мы каждый раз добавляем новые значения, тем самым, рисуя линии.Если их изночально сделать пустыми, то программа не заработает, тк не поймёт тебя

#координата у с которой мы начинаем перебирать точки
y1 = 1

#тот самый садовник, которого мы рассматриваем
x2 = 5
y2 = 5.75

ms = []
ms2 = []
ms3 = []
ms4 = []
ms5 = []
ms6 = []

for q in range(2, 40, 4):
	ms.append(q)

for w in range(3, 40, 4):
	ms2.append(w)

for e in range(0, 40, 4):
	ms3.append(e)

for r in range(1, 40, 4):
	ms4.append(r)

for i in range(10):
	ms5.append(2.5+(i*4))

for i in range(10):
	ms6.append(0.5+(i*4))

#перебор координаты у
for i in tqdm(range(1, 100)):

	#каждый раз, пройдя по строчке, он перемещается в начало строчки и на 0.01 вниз(х снова становится 16, а н увеличивается на 0.01)
	x1 = 2
	y1 += 0.05

	#перебор координаты х
	for j in range(1, 100):
		x = []
		y = []
		massiv = []
		mini_massiv = []

		#massiv - это массив, в который я записываю координаты всех возможных садовников(квадрат а на а(а = кол-во садовников поделённое на два с округлением в большую сторону))
		#mini_massiv - это массив, в который я записываю "а" минимальных координат("а" = кол-во нужных нам садовников)
		s = 0
		i_1 = 0
		for i in range(10):
			if i >= 1:
				s += 1
			for j in range(10):
				if (((i in ms or i in ms2) and j % 2 == 1) or ((i in ms3 or i in ms4) and j % 2 == 0)):
					i_1 = i
					if i%2 == 0:
						i_1-=0.25
					elif i%2 == 1:
						i_1+=0.25
					j_1 = j
					massiv.append((j_1 - x1)**2 + (i_1 - y1)**2)

				if  ((i-0.5 in ms5) and j%2 == 0) or ((i-0.5 in ms6) and j%2 == 1):	
					massiv.append((j - x1)**2 + (i - 0.5 - y1)**2)

		#добавляем координаты в mini_massiv
		for c in range(num_of_gardeners): 
			mini_massiv.append(min(massiv))      
			massiv.remove(min(massiv))

		#добавляем каждый наш шаг по координатам в х и у, для того, чтобы потом это прорисовалось
		if ((x2 - x1)**2 + (y2 - y1)**2) in mini_massiv:
			#добавляем в координату х. Это выглядит так странно, тк именно эта координатная сетка принимает новые значения в х и у только так
			x.append(x1)
			x.append(x1+0.0001)

			y.append(y1)
			y.append(y1+0.0001)

			ax.plot(x, y,color = 'r', linewidth = 1)
		#перемещаемся на следущую координату по х
		x1 += 0.05

s = 0
for i in range(20):
	if i >= 1:
		s += 1
	for j in range(20):
		x = []
		y = []
		if (((i in ms or i in ms2) and j % 2 == 1) or ((i in ms3 or i in ms4) and j % 2 == 0)):
			if s%2 == 0:
				y.append(i-0.25)
				y.append(i-0.2+0.00001)
			elif s%2 == 1:
				y.append(i+0.25)
				y.append(i+0.2+0.00001)				
			x.append(j)
			x.append(j+0.00001)
			#добавляем в координату у

			ax.plot(x, y, color = 'b', linewidth = 1)

		if  ((i-0.5 in ms5) and j%2 == 0) or ((i-0.5 in ms6) and j%2 == 1):
			y.append(i-0.5)
			y.append(i-0.45+0.00001)	

			x.append(j)
			x.append(j+0.00001)
			#добавляем в координату у

			ax.plot(x, y, color = 'b', linewidth = 1)



#дальше рисуется сетка, прописываются координаты и вся остальная визуализация, она работает недолго, так что лучше её не трогать

#открывается окошко
plt.show()





