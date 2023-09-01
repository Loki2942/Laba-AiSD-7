"""
Задание на л.р. №7:
Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода

Задание на л.р. №6:
Вариант 16. На плоскости задано К точек. Сформировать все возможные варианты выбора множества точек
из них для формирования всех возможных треугольников.
В усложненной программе необходимо чтобы сумма координат точки была кратна трём,
затем рассчитать периметр треугольника по координатам,периметр самого большого треугольника, вывести в консоль.
"""
import re
import random
from math import *
from operator import attrgetter

def L(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def combinations(lst, k):
    if k == 0:
        return [[]]
    res = []
    for i in range(len(lst)):
        elem = lst[i]
        rest = lst[i+1:]
        for j in combinations(rest, k-1):
            res.append([elem] + j)
    return res

class Triangle:
    def __init__(self, coordinates):
        self.coordinates = coordinates

class Perimeter:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.perimeter = round(L(x1, y1, x2, y2) + L(x2, y2, x3, y3) + L(x3, y3, x1, y1))

try:
    z = int(input("Введите количество точек (число должно быть больше или равно 3): "))
    while z < 3:  # ошибка в случае введения слишком малого числа
        z = int(input("Вы ввели число, неподходящее по условию, введите число K, большее или равное 3: "))

    n = 25  # это число задаёт диапазон для функции рандом
    pairs = []
    s = 0  # индикатор заполнения
    while s != z:
        # генерируем два случайных числа и добавляем их в список в виде кортежа
        x = random.randint(0, n)
        y = random.randint(0, n)
        # ограничение на характеристики объектов
        if (x + y) % 3 == 0:
            if not (x, y) in pairs:  # защита от одинаковых точек
                pairs.append((x, y))
                s += 1
    print(" \nКординаты точек", pairs)

    m = []
    s = 0
    for j in combinations(pairs, 3):  # составляем комбинаци  z по 3
        m.append(j)
        s += 1

    my_triangles = []
    my_perimeter = []
    for i in m: #здесь i - это треугольник (3 точки)
        i = str(i)
        # ищем в списке i координаты
        x, y = list(map(list, zip(*[list(map(int, pair)) for pair in re.findall(r"\((\d+)\s*,\s*(\d+)\)", i)])))
        # перезапись для формулы
        x1, x2, x3 = x[0], x[1], x[2]
        y1, y2, y3 = y[0], y[1], y[2]

        my_perimeter.append(Perimeter(x1, x2, x3, y1, y2, y3))
        my_triangles.append(Triangle(i))

    for obj in my_triangles:
        print('\nКоординаты возможного треугольника')
        print(obj.coordinates)

    max_attr = max(my_perimeter, key=attrgetter('perimeter'))
    print("\nПериметр самого большого треугольника: ", max_attr.perimeter ,"\n")
    print("\nКоличество возможных треугольников: ", s, "\n")

except ValueError:
    print('\nВы ввели что-то не то, перезапустите программу и следуйте указаниям .')