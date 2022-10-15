

class Dimensions:
    MAX_DIMENSION = 1000
    MIN_DIMENSION = 10
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __setattr__(self, key, value):
        if key=="MAX_DIMENSION" or key=="MIN_DIMENSION":
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

        else:
            object.__setattr__(self, key, value)

    @classmethod
    def proveka(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION


    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.proveka(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.proveka(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.proveka(value):
            self.__c = value

bcd = Dimensions(1, 14, 50)
bcd.a = 2
bcd.b = 1
bcd.c = 1
print(bcd.a, bcd.b, bcd.c)
print(bcd.__dict__)
#print(bcd.MAX_DIMENSION)