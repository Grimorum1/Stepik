class RadiusVector:
    def __init__(self, *args):
        self.coords = [*args]


    def __getitem__(self, item):
        if isinstance(item, int):
            return self.coords[item]
        return tuple(self.coords[item])

    def __setitem__(self, key, value):
        self.coords[key] = value



v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5