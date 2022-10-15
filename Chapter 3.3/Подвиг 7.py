from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args)==1:
            self.spisok = [0 for i in range(*args)]
        else:
            self.spisok = [i for i in args if type(i)==(int or float)]


    def set_coords(self, *args):
        dlina = len(self.spisok)
        for i in range(len(args)):
            if i==dlina:
                break
            self.spisok[i]=args[i]

    def get_coords(self):

        return tuple(self.spisok)


    def __len__(self):
        return len(self.spisok)

    def __abs__(self):
        return sqrt(sum([i*i for i in self.spisok]))

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.get_coords())
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.get_coords())
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
print(vector3D.get_coords())
res_len = len(vector3D) # res_len = 3
print(res_len)
res_abs = abs(vector3D)
print(res_abs)