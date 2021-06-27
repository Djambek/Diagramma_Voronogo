import numpy as np
from tqdm import tqdm
import matplotlib as mpl
#лимит на кол-во точек на рисунке
mpl.rcParams['agg.path.chunksize'] = 10**10000
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

ms = []

weight_of_sites = []

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#кол-во ближайших сайтив (диаграмма какого порядка)
print("введите кол-во ближайших сайтив (диаграмму какого порядка вы хотите получить)")
num_of_gardeners = int(input())


#координаты х и у на графике.В них мы каждый раз добавляем новые значения, тем самым, рисуя точки.
print("введите кол-во сайтов (больше одного)")
num_of_sites = int(input())

strr = 100
step = 0.05
all_ = []

print("введите координаты сайтов. Формат ввода: х1 у1 enter x2 y2 enter...")
for i in range(num_of_sites):
	ms.append((str(input())).split())

print("введите вес сайтов. Формат ввода: z1 enter z2 enter...")
for i in range(num_of_sites):
	weight_of_sites.append(int(input()))

for i in range(num_of_sites):
	for j in range(2):
		ms[i][j] = int(ms[i][j])

		all_.append(ms[i][j])

		if ms[i][j]>=2:
			strr = 200
		if ms[i][j]>10:
			step = 0.1
		if ms[i][j]>50:
			step = 0.5
		if ms[i][j]>100:
			step = 1

#изначальная координата
iznach = min(all_)-3

#координата у с которой мы начинаем перебирать точки
y1 = iznach
x2 = 1
y2 = 1

#перебор координаты у (tqdm определяет на сколько процентов выполнена работа программы)
for i in tqdm(range(1, 200)):

	#каждый раз, пройдя по строчке, он перемещается в начало строчки и на 0.05 вниз
	#(х снова становится изначальной величиной, а у увеличивается на 0.05)
	x1 = iznach
	y1 += step

	#перебор координаты х
	for j in range(1, 200):
		x = []
		y = []
		massiv = []
		mini_massiv = []

		#massiv - это массив, в который мы записываем расстояние от всех возможных сайтов до текущей координаты
		#mini_massiv - это массив, в который мы записываем "num_of_gardeners" минимальных координат
		#("num_of_gardeners" = кол-во нужных нам сайтов)
		for p in range(len(ms)):
			massiv.append(((x1 - ms[p][0])**2 + (y1 - ms[p][1])**2)/weight_of_sites[p]/10)

		#добавляем координаты ближайших сайтов в mini_massiv
		for c in range(num_of_gardeners): 
			mini_massiv.append(min(massiv))      
			massiv.remove(min(massiv))


		#прорисовываем точки из которых в итоге получатся ячейки Вороного
		#(цвет точки зависит от того, какие сайты к ним ближайшие)
		for u in range(len(ms)):
		#if ((x1 - ms[u][0])**2 + (y1 - ms[u][1])**2) in mini_massiv:
			if ((((x1 - ms[u][0])**2 + (y1 - ms[u][1])**2)/weight_of_sites[u]/10)) in mini_massiv:
				x.append(x1)
				x.append(x1+0.0001)

				y.append(y1)
				y.append(y1+0.0001)

				ax.plot(x, y, color = [u/(num_of_sites), u/(num_of_sites), 0.4], linewidth = 1)

		#перемещаемся на следущую координату по х
		x1 += step

#рисуем вершины сетки
for i in range(len(ms)):
	x = []
	y = []

	y.append(ms[i][1])
	y.append(ms[i][1]+0.001)

	x.append(ms[i][0])
	x.append(ms[i][0]+0.001)

	ax.plot(x, y, color = 'b', linewidth = 1)


#открывается окно, в котором вы можете увидеть диаграмму Вороного, построенную по данным вами координатами
plt.show()