#данная программа строит дигарамму Вороного, где сайтами являются отрезки. Она принимает на вход параметры: порядок диаграммы, кол-во сайтов, координаты сайтов и вес каждого сайта.

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
import matplotlib as mpl
from PIL import Image
#лимит на кол-во точек на рисунке
mpl.rcParams['agg.path.chunksize'] = 10**10000
import matplotlib.pyplot as plt
import math
counter = 0
try:
    while 1:
        f = Image.open('answer_for_lines/foo{}.png'.format(counter))
        counter += 1
except:
    pass
my_mas = []
print("Отсчет картинок с номера ", counter)
print("Генерация массива")
#2 четверть как для sin
x = 0
while x<=4:
    y = math.sqrt(16-x*x)
    my_mas.append([0, 0, -x, y])
    x+=0.25
# нормальная генерация 3 четверти 
x = 4
while x>=0:
    y = math.sqrt(16-x*x)
    my_mas.append([0, 0, -x, -y])
    x-=0.25

#нормальная генерация 4 четверти
x = 0
while x<=4:
    y = math.sqrt(16-x*x)
    my_mas.append([0, 0, x, -y])
    x+=0.25

x = 4
while x>=0:
    y = math.sqrt(16-x*x)
    my_mas.append([0, 0, x, y])
    x-=0.25
print("Массив сгенерирован!")
print("Длина массива - ", len(my_mas))
for i in my_mas:
    fig, ax = plt.subplots()

    ms = []

    weight_of_sites = []

    #кол-во ближайших сайтив (диаграмма какого порядка)
    #print("введите кол-во ближайших сайтив (диаграмму какого порядка вы хотите получить)")
    num_of_gardeners = 1


    #print("введите кол-во сайтов (больше одного)")
    num_of_sites = 2

    strr = 100
    step = 0.05
    all_ = []

    #print("введите координаты концов отрезков, которые будут являться сайтами. Формат ввода: х1 у1 x2 y2 enter x3 y3 x4 y4 enter...")
    #for i in range(num_of_sites):
    #    ms.append((str(input())).split())
    ms.append([5, 2, 7, 2])
    ms.append([i[0], i[1], i[2], i[3]])

    for i in range(num_of_sites):
        for j in range(4):
           ms[i][j] = float(ms[i][j]) 

    #print("введите вес сайтов. Формат ввода: z1 enter z2 enter... Если все сайты предполагаемой диаграммы имеют одинаковый вес, то введите 'n'")

    weig = "n"
    if weig == "n" or weig =="'n'" or weig == "т":
        for j in range(num_of_sites):
            weight_of_sites.append(1)
    else:
        weight_of_sites.append(int(weig))
        for i in range(num_of_sites-1):
            weight_of_sites.append(int(input()))

    #просто небольшое удобство
    for i in range(num_of_sites):
        for j in range(2):
            ms[i][j] = int(ms[i][j])

            all_.append(ms[i][j])

            if ms[i][j]>=2:
                strr = 200
            if ms[i][j]>10:
                step = 0.
            if ms[i][j]>50:
                step = 0.5
            if ms[i][j]>100:
                step = 1

    #изначальная координата
    iznach = min(all_)-5

    #координата у с которой мы начинаем перебирать точки
    y1 = iznach
    step = 0.1
    #перебор координаты у (tqdm определяет на сколько процентов выполнена работа программы)
    for i in tqdm(range(1, 150)):

        #каждый раз, пройдя по строчке, он перемещается в начало строчки и на 0.05 вниз
        #(х снова становится изначальной величиной, а у увеличивается на 0.05)
        x1 = iznach
        y1 += step

        #перебор координаты х
        for j in range(1, 150):
            x = []
            y = []
            massiv = []
            mini_massiv = []

            #massiv - это массив, в который мы записываем расстояние от всех возможных сайтов до текущей координаты
            #mini_massiv - это массив, в который мы записываем "num_of_gardeners" минимальных координат
            #("num_of_gardeners" = кол-во нужных нам сайтов)

            for p in range(len(ms)):
                #находим длину отрезка, который является сайтом
                len_of_site = (ms[p][0] - ms[p][2])**2 + (ms[p][1] - ms[p][3])**2
                #print(ms[p])

                #первую сторону
                len_1 = (x1 - ms[p][0])**2 + (y1 - ms[p][1])**2

                #вторую сторону
                len_2 = (x1 - ms[p][2])**2 + (y1 - ms[p][3])**2

                #площадь
                s = abs((ms[p][0]-x1)*(ms[p][3]-y1)-(ms[p][2]-x1)*(ms[p][1]-y1))/2

                #высота
                height = (s*2)/math.sqrt(len_of_site)

                #если треугольник тупоугольный, то находим наименьшее расстояние до конца отрезка
                if (len_1 > len_2 + len_of_site) or (len_2 > len_1 + len_of_site):
                    if len_1 > len_2:
                        dist = math.sqrt(len_2)
                    else:
                        dist = math.sqrt(len_1)

                #в обратном случае находим высоту треугольника
                else:
                    dist = height
                massiv.append(dist/weight_of_sites[p]/10)


            #добавляем координаты ближайших сайтов в mini_massiv
            for c in range(num_of_gardeners): 
                mini_massiv.append(min(massiv))      
                massiv.remove(min(massiv))


            #прорисовываем точки из которых в итоге получатся ячейки Вороного
            #(цвет точки зависит от того, какие сайты к ним ближайшие)
            for u in range(len(ms)):

                len_of_site = (ms[u][0] - ms[u][2])**2 + (ms[u][1] - ms[u][3])**2
                #первую сторону
                len_1 = (x1 - ms[u][0])**2 + (y1 - ms[u][1])**2
                #вторую сторону
                len_2 = ((x1 - ms[u][2])**2 + (y1 - ms[u][3])**2)
                #площадь
                s = abs((ms[u][0]-x1)*(ms[u][3]-y1)-(ms[u][2]-x1)*(ms[u][1]-y1))/2
                
                if (len_1 > len_2 + len_of_site) or (len_2 > len_1 + len_of_site):
                    if len_1 > len_2:
                        dist = math.sqrt(len_2)
                    else:
                        dist = math.sqrt(len_1)

                #в обратном случае находим высоту треугольника
                else:
                    height = (s*2)/math.sqrt(len_of_site)
                    dist = height

                if (dist/weight_of_sites[u]/10) in mini_massiv:
                    x.append(x1)
                    x.append(x1+0.0001)

                    y.append(y1)
                    y.append(y1+0.0001)

                    ax.plot(x, y, color = [u/(num_of_sites), u/(num_of_sites), 0.4], linewidth = 1)

            #перемещаемся на следущую координату по х
            x1 += step

    #рисуем сайты
    for i in range(len(ms)):
        x = []
        y = []

        y.append(ms[i][1])
        y.append(ms[i][1]+0.001)
        y.append(ms[i][3]+0.001)
        y.append(ms[i][3])

        x.append(ms[i][0])
        x.append(ms[i][0]+0.001)
        x.append(ms[i][2])
        x.append(ms[i][2]+0.001)

        ax.plot(x, y, color = 'b', linewidth = 1)   


    #открывается окно, в котором вы можете увидеть диаграмму Вороного, построенную по данным вами координатами
    #plt.show()
    print("Image {} saving".format(counter))
    plt.savefig('answer_for_lines/foo{}.png'.format(counter))
    print("Image {} saved".format(counter))
    counter+=1
print("Programm finished")