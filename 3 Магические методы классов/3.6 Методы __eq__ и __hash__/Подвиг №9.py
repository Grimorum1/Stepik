"""
Подвиг 9 (релакс). Объявите класс с именем Dimensions, объекты которого создаются командой:

d = Dimensions(a, b, c)

где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, ширина и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c (с соответствующими числовыми значениями). Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.

С помощью функции input() прочитайте из входного потока строку, записанную в формате:

"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

Например:

"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

Если какой-либо габарит оказывается отрицательным значением или равен нулю, то при создании объектов должна генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")

Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. После этого отсортируйте этот список по возрастанию (неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.

P.S. На экран ничего выводить не нужно.

Sample Input:

1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5

Sample Output:

"""


class Dimensions:
    def __init__(self, a, b, c):
        if self.proverka(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __str__(self):
        return f"{self.a}-{self.b}-{self.c}"

    def __repr__(self):
        return f"{self.a}-{self.b}-{self.c}"

    @classmethod
    def proverka(cls, *args):
        for i in args:
            if i<=0:
                return False
        return True
    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self)>hash(other)


s_inp = "1 2 3; 4 5 6.78; 1 2 3; 2 1 2.5"

lst_dims = []
for i in s_inp.split(";"):
    x = []
    for j in i.split():
        try:
            x.append(int(j))
        except:
            x.append(float(j))
    lst_dims.append(Dimensions(*x))
print(lst_dims)
lst_dims = sorted(lst_dims, key=lambda x: x.__hash__(), reverse=False)
print(lst_dims)