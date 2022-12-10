"""
Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). Как пример, объявите в программе класс с именем:

Singleton

который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый). Как это делать, вы должны уже знать из этого курса.

Затем, объявите еще один класс с именем:

Game

который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:

game = Game(name)

где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с соответствующим содержимым.

Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так, то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

"""


class Singleton:
    inst = None
    inst_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.inst_base == None:
                cls.inst_base = object.__new__(cls)
            return cls.inst_base

        if cls.inst == None:
            cls.inst = object.__new__(cls)
            return cls.inst
        return cls.inst



class Game(Singleton):

    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name



x = Game("God of War")
y = Game('Dota 2')
print(y.name)
print(x.name)