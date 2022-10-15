from math import sqrt
class Triangle:

    @classmethod
    def proverka(cls, *args):
        for i in args:
            if not isinstance(i, int or float) and not i>0:
                raise ValueError("длины сторон треугольника должны быть положительными числами")
        return True

    @classmethod
    def proverka_2(cls, a, b, c):
        if a < b+c and b < a+c and c < a+b:
            return True
        raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __init__(self, a, b, c):
        if self.proverka(a, b, c) and self.proverka_2(a, b, c):
            self.a = a
            self.b = b
            self.c = c
            self.p = (self.a + self.b + self.c)/2

    def __len__(self):
        return self.a + self.b + self.c


    def __call__(self):
        return sqrt(self.p * (self.p-self.a) * (self.p-self.b) * (self.p-self.c))


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"