class FloatValue:
    @classmethod
    def proverka(cls, value):
        if type(value)!=float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        return True

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.proverka(value):
            instance.__dict__[self.name] = value
            #print(instance.__dict__)

class Cell:
    value = FloatValue()

    def __init__(self, value=3.14):
        self.value = value


class TableSheet:

    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for j in range(m)]for i in range(n)]


c = Cell(12.22)
print(Cell.value)

