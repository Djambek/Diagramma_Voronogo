"""на вход даётся коффиценты 3 уравений прямых ввида y = kx+b. На выходе даётся точка пересечений"""
def peresechenia(k1, b1, k2, b2, k3, b3):
    x1 = -b1/(k1-k2) + b2/(k1-k2)
    y1 = k1(-b1/(k1-k2) + b2/(k1-k2)) + b1
    x2 = -b2/(k2-k3) + b3/(k2-k3)
    y2 = k2(-b2/(k2-k3) + b3/(k2-k3)) + b2
    x3 = -b3/(k3-k1) + b1/(k3-k1)
    y3 = k3(-b3/(k3-k1) + b1/(k3-k1)) + b3
    if x1 == x2 == x3 and y1 == y2 == y3:
        return x1, y1
    else:
        return False
