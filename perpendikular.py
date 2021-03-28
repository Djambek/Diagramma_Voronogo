"""Даются 2 координаты вершины ребра. Ответ даётся в виде уравнения прямой типа y = kx+b """
def per(x1,y1, x2, y2):
    k = (y1-y2)/(x1-x2)
    b = y2 - k*x2
    k_answer = -1/k
    x_ser = (x1+x2)/2
    y_ser = (y1+y2)/2
    b_answer = k_answer*x_ser - y_ser

    return k_answer, b_answer
