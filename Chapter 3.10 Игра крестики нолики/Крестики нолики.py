from random import randint


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple([[Cell() for j in range(3)] for i in range(3)])
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    def init(self):
        self.pole = tuple([[Cell() for j in range(3)] for i in range(3)])

    def proverka(self, key):
        x = []
        y = []
        xy = []
        yx = []
        for i in range(3):
            for j in range(3):
                if self[i, j] == key:
                    x.append(True)
                if self[j, i] == key:
                    y.append(True)
                if self[j, j] == key and len(xy) != 3:
                    xy.append(True)
                if (i in (0, 2) and j in (0, 2) and i != j and (self[i, j]==key or self[j, i]==key)) or (i == 1 and j == 1):
                    yx.append(True)
            if len(x) == 3 or len(y) == 3 or len(xy) or len(yx) == 3:
                return True
            x.clear()
            y.clear()
        return False

    def show(self):
        counter = 0
        for i in self.pole:
            for j in i:
                if counter == 1 or counter == 2:
                    print("|", end="")
                if j.value == self.FREE_CELL:
                    print(" ", end="")
                elif j.value == self.HUMAN_X:
                    print("X", end="")
                else:
                    print("0", end="")
                counter += 1
            print()
            print("_" * 5)
            counter = 0

    def human_go(self):
        x = list(map(int, input("Введите координаты крестика").split()))
        self[x] = 1

    def computer_go(self):
        x = randint(0, 2)
        y = randint(0, 2)
        if self.pole[x][y] == 0:
            self.pole[x][y] = 2
        else:
            self.computer_go()

    def __getitem__(self, item):
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        x, y = key[0], key[1]
        if type(x) != int or type(y) != int or 0 >= x >= 2 or 0 >= y >= 2:
            raise IndexError('некорректно указанные индексы')
        self.pole[x][y].value = value

    def chek_game(self):
        return all([all([j.value == 0 for j in i]) for i in self.pole])

    @property
    def is_human_win(self):
        if self.chek_game():
            return self.__is_human_win
        return self.proverka(1)

    @property
    def is_computer_win(self):
        if self.chek_game():
            return self.__is_computer_win
        return self.proverka(2)

    @property
    def is_draw(self):
        if self.chek_game():
            return self.__is_draw
        return True if not (self.is_human_win or self.is_computer_win) else False

    def __bool__(self):
        return all([all([j.value == 0 for j in i]) for i in self.pole])


class Cell:

    def __init__(self):
        self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return True if self.value == 0 else False






cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
#print(bool(game))
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
print(game.is_human_win, game.is_computer_win, game.is_draw)
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X

assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
print(game.is_human_win)
print(game.is_computer_win)
print(game.is_draw)
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
