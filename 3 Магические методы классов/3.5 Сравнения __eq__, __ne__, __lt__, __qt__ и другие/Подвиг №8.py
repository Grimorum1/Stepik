"""
Подвиг 8. В программе необходимо объявить классы для работы с кошельками в разных валютах:

MoneyR - для рублевых кошельков
MoneyD - для долларовых кошельков
MoneyE - для евро-кошельков

СМОТРИ КАРТИНКУ Подвиг №8

Объекты этих классов могут создаваться командами:

rub = MoneyR()   # с нулевым балансом
dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
euro = MoneyE(100)  # с балансом в 100 евро

В каждом объекте этих классов должны формироваться локальные атрибуты:

__cb - ссылка на класс CentralBank (центральный банк, изначально None);
__volume - объем денежных средств в кошельке (если не указано, то 0).

Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства (property) для работы с локальными атрибутами:

cb - для изменения и считывания данных из переменной __cb;
volume - для изменения и считывания данных из переменной __volume.

Объекты классов должны поддерживать следующие операторы сравнения:

rub < dl
dl >= euro
rub == euro  # значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)
euro > rub

При реализации операторов сравнения считываются соответствующие значения __volume из сравниваемых объектов и приводятся к рублевому эквиваленту в соответствии с курсом валют центрального банка.

Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки, необходимо в программе объявить еще один класс CentralBank. Объекты класса CentralBank создаваться не должны (запретить), при выполнении команды:

cb = CentralBank()

должно просто возвращаться значение None. А в самом классе должен присутствовать атрибут:

rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

Здесь числа (в значениях словаря) - курс валюты по отношению к доллару. 

Также в CentralBank должен быть метод уровня класса:

register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и MoneyE.

При регистрации значение __cb объекта money должно ссылаться на класс CentralBank. Через эту переменную объект имеет возможность обращаться к атрибуту rates класса CentralBank и брать нужные котировки.

Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:

raise ValueError("Неизвестен курс валют.")

Пример использования классов (эти строчки в программе писать не нужно):

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")

P.S. В программе на экран ничего выводить не нужно, только объявить классы.
"""

class CentralBank:

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        if isinstance(money, MoneyD):
            money.cd = cls.rates["dollar"]
        elif isinstance(money, MoneyR):
            money.cd = cls.rates["rub"]
        else:
            money.cd = cls.rates["euro"]
class Deskriptions:

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Current:
    cd = Deskriptions()
    volume = Deskriptions()

    def __init__(self, balance=None):
        self.cd = None
        self.volume = balance if balance != None else 0

    def __eq__(self, other):
        if self.cd != None and other.cd != None:
            x = self.volume/self.cd
            y = other.volume/other.cd
            return abs(x - y) <= abs(0.1)
        raise ValueError("Неизвестен курс валют.")

    def __gt__(self, other):
        if self.cd != None and other.cd != None:
            x = self.volume/self.cd
            y = other.volume/other.cd
            return x>y
        raise ValueError("Неизвестен курс валют.")

    def __ge__(self, other):
        if self.cd != None and other.cd != None:
            x = self.volume/self.cd
            y = other.volume/other.cd
            return x>=y
        raise ValueError("Неизвестен курс валют.")



class MoneyR(Current):
    pass

class MoneyD(Current):
    pass

class MoneyE(Current):
    pass











r = MoneyD(500.00005)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

print(r==d)