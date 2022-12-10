"""
Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)

где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает

При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')

P.S. В программе на экран выводить ничего не нужно, только объявить класс.

"""

class Vector:
    def __init__(self, *args):
        self.coord = [*args]

    def __add__(self, other):
        if len(self.coord) == len(other.coord):
            res = [self.coord[i] + other.coord[i] for i in range(len(self.coord))]
            return Vector(*res)
        raise ArithmeticError('размерности векторов не совпадают')

    def __iadd__(self, other):
        if isinstance(other, Vector):
            if len(self.coord) == len(other.coord):
                self.coord = [self.coord[i] + other.coord[i] for i in range(len(self.coord))]
                return self
            raise ArithmeticError('размерности векторов не совпадают')
        self.coord = [other + i for i in self.coord]
        return self

    def __sub__(self, other):
        if len(self.coord) == len(other.coord):
            res = [self.coord[i] - other.coord[i] for i in range(len(self.coord))]
            return Vector(*res)
        raise ArithmeticError('размерности векторов не совпадают')

    def __isub__(self, other):
        if isinstance(other, Vector):
            if len(self.coord) == len(other.coord):
                self.coord = [self.coord[i] - other.coord[i] for i in range(len(self.coord))]
                return self
            raise ArithmeticError('размерности векторов не совпадают')
        self.coord = [i - other for i in self.coord]
        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coord) == len(other.coord):
                res = [self.coord[i] * other.coord[i] for i in range(len(self.coord))]
                return Vector(*res)
            raise ArithmeticError('размерности векторов не совпадают')
        res = [i * other for i in self.coord]
        return Vector(*res)

    def __eq__(self, other):
        return self.coord == other.coord


v1 = Vector(6, 6, 6)
v2 = Vector(3, 3, 3)
v1 -= v2
print(v1.coord)
v3 = v1 == v2
print(v3)
