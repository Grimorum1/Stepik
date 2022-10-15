from random import randint
class Deskription:


    @classmethod
    def proverka(cls, name, value):
        if name in ("__is_mine", "__is_open") and value in (True, False):
            return True
        elif name=="__number" and 0<=value<=8:
            return True
        else:
            return False


    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return owner.__dict__[self.name]

    def __set__(self, instance, value):
        #if self.proverka(self.name, value):
        instance.__dict__[self.name] = value
        # else:
        #     raise ValueError("недопустимое значение атрибута")


class Cell:

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @classmethod
    def proverka(cls, name, value):
        if name in ("is_mine", "is_open") and value in (True, False):
            return True
        elif name == "number" and 0 <= value <= 8:
            return True
        else:
            return False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if self.proverka("is_mine", value):
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if self.proverka("number", value):
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if self.proverka("is_open", value):
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return bool(not self.is_open)


class GamePole:
    __inst = None
    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple([tuple([Cell() for j in range(M)]) for i in range(N)])

    def __new__(cls, *args, **kwargs):
        if cls.__inst == None:
            cls.__inst = super().__new__(GamePole)
            return cls.__inst
        return cls.__inst


    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        count = self.total_mines
        while count!=0:
            x = randint(0, self.N-1)
            y = randint(0, self.M-1)
            #print(count)
            if self.__pole_cells[x][y].is_mine:
                continue
            self.__pole_cells[x][y].is_mine = True
            self.__pole_cells[x][y].number = 0
            count -=1
            y = [c for c in [y - 1, y, y + 1] if 0 <= c <= self.M-1]
            x = [c for c in [x - 1, x, x + 1] if 0 <= c <= self.N-1]
            for i in x:
                for j in y:
                    if not self.__pole_cells[i][j].is_mine:
                        self.__pole_cells[i][j].number +=1



    def open_cell(self, i, j):
        if 0<=i<=self.N and 0<=j<=self.M:
            self.__pole_cells[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for i in self.__pole_cells:
            for j in i:
                if j.is_open:
                    if j.is_mine:
                        print("*", end=" ")
                    else:
                        print(j.number, end=" ")
                else:
                    print("=", end=" ")
            print()


p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"