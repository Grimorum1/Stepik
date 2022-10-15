class Vector:
    def __init__(self, *args):
        self.coord = [*args]

    def __add__(self, other):
        if len(self.coord) == len(other.coord):
            res = [self.coord[i] + other.coord[i] for i in range(len(self.coord))]
            return Vector(*res)
        raise ArithmeticError('размерности векторов не совпадают')

    def __iadd__(self, other):
        if isinstance(other, Vector):
            if len(self.coord) == len(other.coord):
                self.coord = [self.coord[i] + other.coord[i] for i in range(len(self.coord))]
                return self
            raise ArithmeticError('размерности векторов не совпадают')
        self.coord = [other + i for i in self.coord]
        return self

    def __sub__(self, other):
        if len(self.coord) == len(other.coord):
            res = [self.coord[i] - other.coord[i] for i in range(len(self.coord))]
            return Vector(*res)
        raise ArithmeticError('размерности векторов не совпадают')

    def __isub__(self, other):
        if isinstance(other, Vector):
            if len(self.coord) == len(other.coord):
                self.coord = [self.coord[i] - other.coord[i] for i in range(len(self.coord))]
                return self
            raise ArithmeticError('размерности векторов не совпадают')
        self.coord = [i - other for i in self.coord]
        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coord) == len(other.coord):
                res = [self.coord[i] * other.coord[i] for i in range(len(self.coord))]
                return Vector(*res)
            raise ArithmeticError('размерности векторов не совпадают')
        res = [i * other for i in self.coord]
        return Vector(*res)

    def __eq__(self, other):
        return self.coord == other.coord


v1 = Vector(6, 6, 6)
v2 = Vector(3, 3, 3)
v1 -= v2
print(v1.coord)
v3 = v1 == v2
print(v3)
