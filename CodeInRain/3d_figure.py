from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from tqdm import tqdm

fig = plt.figure()
ax = fig.gca(projection='3d')

#кол-во садовников
num_of_gardeners = 2

#координаты х и у на графике.В них мы каждый раз добавляем новые значения, тем самым, рисуя линии.Если их изночально сделать пустыми, то программа не заработает, тк не поймёт тебя
X = [20, 20]
Y = [20, 20]
Z = [20, 20]

#координата у с которой мы начинаем перебирать точки
z1 = 17

#тот самый садовник, которого мы рассматриваем
x2 = 20
y2 = 20
z2 = 20

x3 = 20
y3 = 20
z3 = 19

col = 0

for i in tqdm(range(1, 100)):
	y1 = 17
	z1 += 0.05

	for j in range(1, 100):
		col += 0.0002
		x1 = 17
		y1 += 0.05

		for h in range(1, 100):
			X = []
			Y = []
			Z = [] 

			massiv = [((round(x1) - x1)**2 + (round(y1) - y1)**2 + (round(z1) - z1)**2)]
			mini_massiv = []

			#massiv - это массив, в который я записываю координаты всех возможных садовников(квадрат а на а(а = кол-во садовников поделённое на два с округлением в большую сторону))
			#mini_massiv - это массив, в который я записываю "а" минимальных координат("а" = кол-во нужных нам садовников)

			#добавляем координаты в massiv
			for n in range(1, num_of_gardeners//2 + 2):

				massiv.append((round(x1) - x1)**2 + (round(y1+n) - y1)**2 + (round(z1) - z1)**2)
				massiv.append((round(x1) - x1)**2 + (round(y1-n) - y1)**2 + (round(z1) - z1)**2)

				massiv.append((round(x1+n) - x1)**2 + (round(y1) - y1)**2 + (round(z1) - z1)**2)
				massiv.append((round(x1-n) - x1)**2 + (round(y1) - y1)**2 + (round(z1) - z1)**2)

				massiv.append((round(x1) - x1)**2 + (round(y1) - y1)**2 + (round(z1+n) - z1)**2)
				massiv.append((round(x1) - x1)**2 + (round(y1) - y1)**2 + (round(z1-n) - z1)**2)

				for n_2 in range(1, num_of_gardeners//2 + 2):

					massiv.append((round(x1) - x1)**2 + (round(y1+n) - y1)**2 + (round(z1-n_2) - z1)**2)
					massiv.append((round(x1) - x1)**2 + (round(y1+n) - y1)**2 + (round(z1+n_2) - z1)**2)
					massiv.append((round(x1) - x1)**2 + (round(y1-n) - y1)**2 + (round(z1+n_2) - z1)**2)
					massiv.append((round(x1) - x1)**2 + (round(y1-n) - y1)**2 + (round(z1-n_2) - z1)**2)

					massiv.append((round(x1+n) - x1)**2 + (round(y1) - y1)**2 + (round(z1+n_2) - z1)**2)
					massiv.append((round(x1+n) - x1)**2 + (round(y1) - y1)**2 + (round(z1-n_2) - z1)**2)
					massiv.append((round(x1-n) - x1)**2 + (round(y1) - y1)**2 + (round(z1+n_2) - z1)**2)
					massiv.append((round(x1-n) - x1)**2 + (round(y1) - y1)**2 + (round(z1-n_2) - z1)**2)
					
					massiv.append((round(x1+n) - x1)**2 + (round(y1+n_2) - y1)**2 + (round(z1) - z1)**2)
					massiv.append((round(x1+n) - x1)**2 + (round(y1-n_2) - y1)**2 + (round(z1) - z1)**2)
					massiv.append((round(x1-n) - x1)**2 + (round(y1+n_2) - y1)**2 + (round(z1) - z1)**2)
					massiv.append((round(x1-n) - x1)**2 + (round(y1-n_2) - y1)**2 + (round(z1) - z1)**2)

					for n_3 in range(1, num_of_gardeners//2 + 2):

						massiv.append((round(x1+n) - x1)**2 + (round(y1+n_2) - y1)**2 + (round(z1+n_3) - z1)**2)
						massiv.append((round(x1+n) - x1)**2 + (round(y1+n_2) - y1)**2 + (round(z1-n_3) - z1)**2)
						massiv.append((round(x1-n) - x1)**2 + (round(y1+n_2) - y1)**2 + (round(z1+n_3) - z1)**2)
						massiv.append((round(x1-n) - x1)**2 + (round(y1+n_2) - y1)**2 + (round(z1-n_3) - z1)**2)

						massiv.append((round(x1+n) - x1)**2 + (round(y1-n_2) - y1)**2 + (round(z1+n_3) - z1)**2)
						massiv.append((round(x1+n) - x1)**2 + (round(y1-n_2) - y1)**2 + (round(z1-n_3) - z1)**2)
						massiv.append((round(x1-n) - x1)**2 + (round(y1-n_2) - y1)**2 + (round(z1+n_3) - z1)**2)
						massiv.append((round(x1-n) - x1)**2 + (round(y1-n_2) - y1)**2 + (round(z1-n_3) - z1)**2)


			for c in range(num_of_gardeners): 
				mini_massiv.append(min(massiv))      
				massiv.remove(min(massiv))

			if ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) in mini_massiv:

				#добавляем в координату х. Это выглядит так странно, тк именно эта координатная сетка принимает новые значения в х и у только так
				X.append(x1)
				X.append(x1 + 0.001)

				Y.append(y1)
				Y.append(y1 + 0.001)

				Z.append(z1)
				Z.append(z1 + 0.001)

				ax.plot(X, Y, Z, c=(0, col/2, 0))

			"""if ((x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2) in mini_massiv:

				#добавляем в координату х. Это выглядит так странно, тк именно эта координатная сетка принимает новые значения в х и у только так
				X.append(x1)
				X.append(x1 + 0.001)

				Y.append(y1)
				Y.append(y1 + 0.001)

				Z.append(z1)
				Z.append(z1 + 0.001)

				ax.plot(X, Y, Z, c=(col/2, 0, 0))"""
			#перемещаемся на следущую координату по х
			x1 += 0.05


plt.show()
