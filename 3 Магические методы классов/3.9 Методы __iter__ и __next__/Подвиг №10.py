"""
Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:

m1 = Matrix(rows, cols, fill_value)

где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы (должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

Также объекты можно создавать командой:

m2 = Matrix(list2D)

где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')

Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение

Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')

Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать исключение:

raise IndexError('недопустимые значения индексов')

Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1

Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')

Пример для понимания использования индексов (эти строчки в программе писать не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

"""


class Matrix:
    def __init__(self, *args):
        if self.proverka(args):
            self.rows = len(args[0])
            self.cols = len(args[0][1])
            self.spisok = args[0]
        else:
            self.rows, self.cols, self.fill_value = args
            self.spisok = [[self.fill_value for j in range(self.cols)] for i in range(self.rows)]

    def proverka(self, args):
        spisok = args[0]
        if len(args) == 1:
            if len(max(spisok)) == len(min(spisok)):
                for i in spisok:
                    for j in i:
                        if type(j) not in (int, float):
                            raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            else:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            return True
        else:
            if type(args[0]) != int or type(args[1]) != int or type(args[2]) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            return False

    def __getitem__(self, item):
        if type(item[0]) == int and type(item[1]) == int:
            if (0 <= item[0] <= self.cols) and (0 <= item[1] <= self.cols):
                return self.spisok[item[0]][item[1]]
        raise IndexError('недопустимые значения индексов')

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        if type(key[0]) == int and type(key[1]) == int:
            if (0 <= key[0] <= self.cols) and (0 <= key[1] <= self.cols):
                self.spisok[key[0]][key[1]] = value
                return True
        raise IndexError('недопустимые значения индексов')

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            spisok = [[(self.spisok[j][i] + other.spisok[j][i]) for i in range(self.cols)] for j in range(self.rows)]
            return Matrix(spisok)
        else:
            spisok = [[(self.spisok[j][i] + other) for i in range(self.cols)] for j in range(self.rows)]
            return Matrix(spisok)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            spisok = [[(self.spisok[j][i] - other.spisok[j][i]) for i in range(self.cols)] for j in range(self.rows)]
            return Matrix(spisok)
        else:
            spisok = [[(self.spisok[j][i] - other) for i in range(self.cols)] for j in range(self.rows)]
            return Matrix(spisok)





