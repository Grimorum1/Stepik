"""
Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:

bag = Bag(max_weight)

где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)

где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение). В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе, генерируется исключение:

raise ValueError('превышен суммарный вес предметов')

Также с объектами класса Bag должны выполняться следующие команды:

t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del bag[indx] # удаление вещи из сумки, расположенной по индексу indx

Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

raise IndexError('неверный индекс')

Пример использования классов (эти строчки в программе не писать):

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

"""

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.weight = 0
        self.bag = []

    def add_thing(self, thing):
        if self.max_weight<self.weight + thing.weight:
            raise ValueError('превышен суммарный вес предметов')
        self.bag.append(thing)
        self.weight += thing.weight


    def __getitem__(self, item):
        if 0>item>len(self.bag) :
            raise IndexError('неверный индекс')
        return self.bag[item]

    def __setitem__(self, key, value):
        if 0>key>len(self.bag) :
            raise IndexError('неверный индекс')
        if self.weight - self.bag[key].weight + value.weight>self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.weight = self.weight - self.bag[key].weight + value.weight
        self.bag[key]=value

    def __delitem__(self, key):
        self.weight -= self.bag[key].weight
        del self.bag[key]



class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight





b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"