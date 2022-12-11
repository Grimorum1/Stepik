"""


Подвиг 9 (на повторение). Вам поручают разработать класс для представления маршрутов в навигаторе. Для этого требуется объявить класс с именем Track, объекты которого могут создаваться командами:

tr = Track(start_x, start_y)
tr = Track(pt1, pt2, ..., ptN)

где start_x, start_y - начальная координата маршрута (произвольные числа); pt1, pt2, ..., ptN - набор из произвольного числа точек (координат) маршрута (объекты класса PointTrack).

При передаче аргументов (start_x, start_y) координата должна представляться первым объектом класса PointTrack. Наборы всех точек (объектов PointTrack) должны сохраняться в локальном приватном атрибуте объекта класса Track:

__points - список из точек (координат) маршрута.

Далее, каждая точка (координата) должна определяться классом PointTrack, объекты которого создаются командой:

pt = PointTrack(x, y)

где x, y - числа (целые или вещественные). Если передается другой тип данных, то должно генерироваться исключение командой:

raise TypeError('координаты должны быть числами')

В классе PointTrack переопределите магический метод __str__, чтобы информация об объекте класса возвращалась в виде строки:

"PointTrack: <x>, <y>"

Например:

pt = PointTrack(1, 2)
print(pt) # PointTrack: 1, 2

В самом классе Track должно быть свойство (property) с именем:

points - для получения кортежа из точек маршрута.

Также в классе Track должны быть методы:

def add_back(self, pt) - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
def add_front(self, pt) - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
def pop_back(self) - удаление последней точки из маршрута;
def pop_front(self) - удаление первой точки из маршрута.

Пример использования классов (эти строчки в программе писать не нужно):

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.

"""

class Track:

    def __init__(self, *args):
        self.__points = [i for i in args]


    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)


    def add_front(self, pt):
        self.__points.insert(0, pt)


    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points = self.__points[1:]

class PointTrack:

    def __init__(self, x, y):
        if (type(x) not in (int, float)) or (type(y) not in (int, float)):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y


    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)