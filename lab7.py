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


def combinations(lst, k): # составляем все возможные сочетания точек
    if k == 0:
        return [[]]
    res = []
    for i in range(len(lst)):
        elem = lst[i]
        rest = lst[i+1:]
        for j in combinations(rest, k-1):
            res.append([elem] + j)
    return res


class Points():
    def __init__(self):
        s = 0
        while s != 1:
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            # ограничение на характеристики объектов
            if (x + y) % 3 == 0:
                s +=1
                self.coordinates = (x, y)
    def __str__(self):
        return str(self.coordinates)


class Perimeter():
    def length(self, x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def __init__(self, i):
        i = (' '.join(map(str, i)))
        # ищем в списке i координаты
        x, y = list(map(list, zip(*[list(map(int, pair)) for pair in re.findall(r"\((\d+)\s*,\s*(\d+)\)", i)])))
        x1, x2, x3 = x[0], x[1], x[2]
        y1, y2, y3 = y[0], y[1], y[2]
        perimeter = round(self.length(x1, y1, x2, y2) + self.length(x2, y2, x3, y3) + self.length(x3, y3, x1, y1))
        self.perimeter = perimeter

    def __str__(self):
        return str(self.perimeter)

try:
    z = int(input("Введите количество точек (число должно быть больше или равно 3): "))
    while z < 3:  # ошибка в случае введения слишком малого числа
        z = int(input("Вы ввели число, неподходящее по условию, введите число K, большее или равное 3: "))

    set_of_points = [] # создаем список экземпляров класса
    for i in range(z):
        set_of_points.append(Points())
    print("\nКоличество точек:", z)
    print("\nКоординаты точек:")
    for i in set_of_points:
        print(i)
    print("\n")

    m = []
    for j in combinations(set_of_points, 3):  # составляем комбинаци  z по 3
        m.append(j)

    print('Координаты точек возможных треугольников:\n')
    my_perimeter = []
    for i in m:
        print(' Точка № 1: {}, Точка № 2: {}, Точка № 3: {}\n'.format(*i))
        perimeter = Perimeter(i)
        my_perimeter.append(perimeter)

    max_attr = max(my_perimeter, key=attrgetter('perimeter')) # поиск максимального значения в списке экземпляров класса Perimeter
    print("\nПериметр самого большого треугольника: ", max_attr.perimeter ,"\n")

except ValueError:
    print('\nВы ввели неподходящее значение, перезапустите программу и следуйте указаниям.')

