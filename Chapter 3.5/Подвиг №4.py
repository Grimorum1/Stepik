class DimensionsDescriptors:

    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__validate(instance, value):
            setattr(instance, self.name, value)

    @staticmethod
    def __validate(instance, value):
        return instance.MIN_DIMENSION <= value <= instance.MAX_DIMENSION


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    a = DimensionsDescriptors()
    b = DimensionsDescriptors()
    c = DimensionsDescriptors()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def volume(self):
        return (self.a * self.b * self.c)



    def __lt__(self, other):
        return (self.a * self.b * self.c) < (other.a * other.b * other.c)

    def __le__(self, other):
        return (self.a * self.b * self.c) <= (other.a * other.b * other.c)

class ShopItem:

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


c = Dimensions(40, 30, 120)
trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key= lambda x: x.dim.volume())

assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

lst_sp = []
lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
s = [x.name for x in lst_shop_sorted]
assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)
assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10
assert d2 < d1, "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"