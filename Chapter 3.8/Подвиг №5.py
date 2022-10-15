

class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, ower):
        return getattr(instance, self.name)
        # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)
        # instance.__dict__[self.name] = value

class CellInteger:

    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

class TableValues:

    def __init__(self, rows, cols, cell=None):
        self._rows = rows
        self._cols = cols
        if cell==None:
            raise ValueError('параметр cell не указан')
        self.cells = tuple(tuple(cell() for j in range(self._cols)) for i in range(self._rows))

    def __getitem__(self, item):
        res = self.cells[item[0]][item[1]].value
        return res

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value






tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"
