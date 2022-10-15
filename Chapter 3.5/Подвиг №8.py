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