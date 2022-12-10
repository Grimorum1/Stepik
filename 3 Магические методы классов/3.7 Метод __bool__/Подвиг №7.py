"""

Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)

где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла. Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2. Вторая команда создает объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.

В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все локальные атрибуты x1, y1, x2, y2 существуют и False - в противном случае.

Также в классе Ellipse нужно реализовать метод:

get_coords() - для получения кортежа текущих координат объекта.

Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() должен генерировать исключение командой:

raise AttributeError('нет координат для извлечения')

Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse. Два объекта должны быть созданы командой 

Ellipse()

и еще два - командой:

Ellipse(x1, y1, x2, y2)

Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих координаты x1, y1, x2, y2. (Помните, что для этого был определен магический метод __bool__()).

P.S. На экран ничего выводить не нужно.

"""

class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if x1 and x2 and y1 and y2:
            self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2


    def __bool__(self):
        if len(self.__dict__)>0:
            if not bool(self.x1):
                return False
            if not bool(self.x2):
                return False
            if not bool(self.y2):
                return False
            if not bool(self.y1):
                return False
            return True
        return False

    def get_coords(self):
        if bool(self):
            return (self.x1, self.y1, self.x2, self.y2)
        raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 4, 4), Ellipse(1, 1, 5, 5)]
for i in lst_geom:
    if bool(i):
        i.get_coords()
