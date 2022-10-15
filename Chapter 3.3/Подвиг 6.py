from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img


    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value)!=(int or float):
            raise ValueError("Неверный тип данных.")
        else:
            self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) != (int or float):
            raise ValueError("Неверный тип данных.")
        else:
            self.__img = value

    def __abs__(self):
        return sqrt(self.real*self.real + self.img*self.img)


cm = Complex(7, 8)
cm.real = 3
cm.img = 4
c_abs = abs(cm)
print(c_abs)