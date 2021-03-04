import numpy as np
from tqdm import tqdm
import matplotlib as mpl
#лимит на кол-во точек на рисунке
mpl.rcParams['agg.path.chunksize'] = 10**10000
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

#вершины, которые нам даны
ms = [[1, 1], [0, 0], [1, 2], [2, 1]]

#рисуем рёбра
for i in range(len(ms)):
	x = []
	y = []

	y.append(ms[i][1])
	y.append(ms[i][1]+0.001)

	x.append(ms[i][0])
	x.append(ms[i][0]+0.001)

	y.append(ms[0][1])
	y.append(ms[0][1]+0.001)

	x.append(ms[0][0])
	x.append(ms[0][0]+0.001)

	ax.plot(x, y, color='r', linewidth=1)

#рисуем окружность
def circle(ms):
	massiv_of_segments = []
	massiv_of_seg = []

	#находим длину отрезков
	for i in range(1, len(ms)):
		x1 = ms[0][0] - ms[i][0]
		y1 = ms[0][1] - ms[i][1]
		segment_length = math.sqrt(x1**2 + y1**2)
		#массив длин векторов
		massiv_of_segments.append(segment_length)
		#массив векторов
		massiv_of_seg.append([x1, y1])

	#радиус окружности
	r_of_circle = min(massiv_of_segments)

	#рисуем окружность
	circ = plt.Circle((ms[0][0], ms[0][1]), radius=r_of_circle-0.01, edgecolor='b', facecolor='None')
	ax.add_patch(circ)

	#plt.show()

	angles_between_edges(ms = ms, massiv_of_segments = massiv_of_segments, massiv_of_seg = massiv_of_seg, r_of_circle = r_of_circle)

#находим уголы между рёбрами
def angles_between_edges(ms, massiv_of_segments, massiv_of_seg, r_of_circle):
	#массив, где мы будем хранить углы между рёбрами
	ygol = []
	#добавляем в массив угол между первым и последним ребром
	ygol.append((math.acos((massiv_of_seg[0][0]*massiv_of_seg[-1][0] + massiv_of_seg[0][1]*massiv_of_seg[-1][1])/(massiv_of_segments[0]*massiv_of_segments[-1])))/math.pi*180)
	#добавляем в массив углы между рёбрами
	for i in range(1, len(massiv_of_seg)):
		ygol.append((math.acos((massiv_of_seg[i-1][0]*massiv_of_seg[i][0] + massiv_of_seg[i-1][1]*massiv_of_seg[i][1])/(massiv_of_segments[i-1]*massiv_of_segments[i])))/math.pi*180)
	sides_of_triangle(ms=ms, r_of_circle = r_of_circle, ygol = ygol)

#находим длины сторон треугольника
def sides_of_triangle(ms, r_of_circle, ygol):
	sides = []
	for i in range(len(ygol)):
		#узнаём стороны
		sides.append(2*r_of_circle*(math.sin(180-ygol[i])))
		print(sides)

circle(ms)
class Draw_obratnai():
	def __init__(self, koor_toch):
		self.center = koor_toch[0]
		self.koor_toch = koor_toch

	def circle(self):
		massiv_of_segments = []
		massiv_of_seg = []

		#находим длину отрезков
		for i in range(1, len(self.koor_toch)):
			x1 = self.koor_toch[0][0] - self.koor_toch[i][0]
			y1 = self.koor_toch[0][1] - self.koor_toch[i][1]
			segment_length = math.sqrt(x1**2 + y1**2)
			#массив длин векторов
			massiv_of_segments.append(segment_length)
			#массив векторов
			massiv_of_seg.append([x1, y1])

		#радиус окружности
		r_of_circle = min(massiv_of_segments)

		#рисуем окружность
		circ = plt.Circle((self.koor_toch[0][0], self.koor_toch[0][1]), radius=r_of_circle-0.01, edgecolor='b', facecolor='None')
		ax.add_patch(circ)
		return  r_of_circle

	def angles_between_edges(ms, massiv_of_segments, massiv_of_seg):
		# массив, где мы будем хранить углы между рёбрами
		ygol = []
		# добавляем в массив угол между первым и последним ребром
		ygol.append((math.acos(
			(massiv_of_seg[0][0] * massiv_of_seg[-1][0] + massiv_of_seg[0][1] * massiv_of_seg[-1][1]) / (
						massiv_of_segments[0] * massiv_of_segments[-1]))) / math.pi * 180)
		# добавляем в массив углы между рёбрами
		for i in range(1, len(massiv_of_seg)):
			ygol.append((math.acos(
				(massiv_of_seg[i - 1][0] * massiv_of_seg[i][0] + massiv_of_seg[i - 1][1] * massiv_of_seg[i][1]) / (
							massiv_of_segments[i - 1] * massiv_of_segments[i]))) / math.pi * 180)
		return ygol

	def sides_of_triangle(ms, r_of_circle, ygol):
		sides = []
		for i in range(len(ygol)):
			# узнаём стороны
			sides.append(2 * r_of_circle * (math.sin(180 - ygol[i])))
			print(sides)
			# p = (sides[0]+sides[1]+sides[2]) / 2
			# height = (2*math.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2])))/sides[0]
			# koor_trey = [[self.center[0]+(sides[2]/2), self.center[1]+(sidess)]]
			return sides

	def per(self, x1, y1, x2, y2): # тут просто надо дать вершины, которые дали в начале. Потом на выходе получим уравнения прямой. Подставим x(начальное) + длинна стороны. И получим сё на выходе
		k = (y1 - y2) / (x1 - x2)
		b = y2 - k * x2
		k_answer = -1 / k
		x_ser = (x1 + x2) / 2
		y_ser = (y1 + y2) / 2
		b_answer = k_answer * x_ser - y_ser

		return k_answer, b_answer

	def koor_triangle(self, k, b, x_centre, len_storon):
		y1 = k*(x_centre+len_storon/2) + b
		x1 = x_centre+len_storon/2
		y2 = k*(x_centre-len_storon/2) + b
		x2 = x_centre-len_storon/2
		return x1, y1, x2, y2
	def return_straight(self, x1,y1, x2, y2):
		# возваращают прямую по 2 точкам!
		k = (y1 - y2) / (x1 - x2)
		b = y2 - k * x2
		return k, b

# Даём на вход координаты ребер
# Получаем на выход радиус окружности
# даём радиус на вход и находим стороны треугольника
# получаем координаты точек, где находятся эти стороны
# вызываем функцию и даём туда координаты точек, возвращает прямую
# Делаем все это, но только для другой тройки ребер (которые рядом)
# кидаем в функцию 2 прямые от одного результата работы класса и второго
# получаем точку пересечения
# узнаём радиус окружности, и находим оставшиеся точки!

