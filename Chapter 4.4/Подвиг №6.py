class Furniture:

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __verify_name(self):
        if type(self._name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self):
        if 0 > self._weight:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if key == "_name":
            self.__verify_name()
        else:
            self.__verify_weight()


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return self.__dict__.values()

class Chair(Furniture):

    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return self.__dict__.values()



class Table(Furniture):

    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return tuple(self.__dict__.values())

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())