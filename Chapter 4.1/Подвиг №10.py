class Vector:

    def __init__(self, *args):
        self.spisok = tuple(i for i in args)


    def __add__(self, other):
        if len(self.spisok)!=len(other.spisok):
            raise TypeError('размерности векторов не совпадают')
        if type(other) == Vector:
            return Vector(*[self.spisok[i] + other.spisok[i] for i in range(len(self.spisok))])
        return VectorInt(*[self.spisok[i] + other.spisok[i] for i in range(len(self.spisok))])


    def __sub__(self, other):
        if len(self.spisok) != len(other.spisok):
            raise TypeError('размерности векторов не совпадают')
        if type(other) == Vector:
            return Vector(*[self.spisok[i] - other.spisok[i] for i in range(len(self.spisok))])
        return VectorInt(*[self.spisok[i] - other.spisok[i] for i in range(len(self.spisok))])

    def get_coords(self):
        return tuple(i for i in self.spisok)



class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__()
        self.spisok = []
        for i in args:
            if type(i)==int:
                self.spisok.append(i)
            else:
                raise ValueError('координаты должны быть целыми числами')


v1 = Vector(1.0, 2, 3)
v2 = VectorInt(3, 4, 5)
v3 = v1 + v2
print(type(v3))