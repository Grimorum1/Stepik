"""
Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)

где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами

Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')

В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')

При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt

должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. Иначе, v должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

"""

class Vector:

    def __init__(self, *args):
        self.spisok = tuple(i for i in args)


    def __add__(self, other):
        if len(self.spisok)!=len(other.spisok):
            raise TypeError('размерности векторов не совпадают')
        if type(other) == Vector:
            return Vector(*[self.spisok[i] + other.spisok[i] for i in range(len(self.spisok))])
        return VectorInt(*[self.spisok[i] + other.spisok[i] for i in range(len(self.spisok))])


    def __sub__(self, other):
        if len(self.spisok) != len(other.spisok):
            raise TypeError('размерности векторов не совпадают')
        if type(other) == Vector:
            return Vector(*[self.spisok[i] - other.spisok[i] for i in range(len(self.spisok))])
        return VectorInt(*[self.spisok[i] - other.spisok[i] for i in range(len(self.spisok))])

    def get_coords(self):
        return tuple(i for i in self.spisok)



class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__()
        self.spisok = []
        for i in args:
            if type(i)==int:
                self.spisok.append(i)
            else:
                raise ValueError('координаты должны быть целыми числами')


