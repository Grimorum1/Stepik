class Digit:
    def __init__(self, value):
        if self.chek_value(value):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

    def chek_value(self, value):
        if type(value) not in (int, float):
            return True
        return False


class Integer(Digit):

    def chek_value(self, value):
        if type(value) != int or super().chek_value(value):
            return True
        return False


class Float(Digit):
    def chek_value(self, value):
        if type(value) != float or super().chek_value(value):
            return True
        return False


class Positive(Digit):
    def chek_value(self, value):
        if value < 0 or super().chek_value(value):
            return True

        return False


class Negative(Digit):
    def chek_value(self, value):
        if value >= 0 or super().chek_value(value):
            return True
        return False


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass

digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4),
          FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
print(lst_float, lst_positive, sep='\n')