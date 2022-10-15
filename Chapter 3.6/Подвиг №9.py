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