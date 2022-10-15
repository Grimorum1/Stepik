class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3))for _ in range(3))

    def clear(self):
        for i in self.pole:
            for j in i:
                j.value = 0
                j.is_free = False

    def __getitem__(self, item):
        if isinstance(item[0], slice):
            res = tuple(i[item[1]].value for i in self.pole[item[0]])
            return res
        elif isinstance(item[1], slice):
            res = tuple(i.value for i in self.pole[item[0]][item[1]])
            return res
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if key[0]>2 or key[1]>2:
            raise IndexError('неверный индекс клетки')
        if self.pole[key[0]][key[1]].is_free:
            raise ValueError('клетка уже занята')
        self.pole[key[0]][key[1]].value = value



class Cell:
    def __init__(self, is_free=True, value=0):
        self.is_free = is_free
        self.value = value

    def __bool__(self):
        return bool(self.is_free)


