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