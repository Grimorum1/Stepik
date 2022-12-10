"""
Подвиг 9 (на повторение). Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса StringDigit должны создаваться командой:

sd = StringDigit(string)

где string - строка из цифр (например, "12455752345950"). Если в строке string окажется хотя бы один не цифровой символ, то генерировать исключение командой:

raise ValueError("в строке должны быть только цифры")

Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции:

sd = sd + "123"
sd = "123" + sd

создавали новые объекты класса StringDigit (а не класса str). Если же при соединении строк появляется не цифровой символ, то генерировать исключение:

raise ValueError("в строке должны быть только цифры")

Пример использования класса (эти строчки в программе не писать):

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError

P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.

"""

class StringDigit(str):

    def __init__(self, string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")


    def __add__(self, other):
        x = StringDigit(other)
        x = super().__add__(x)
        return StringDigit(x)

    def __radd__(self, other):
        x = StringDigit(other)
        return x + self


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
print(type(sd), sd)
sd = "789" + sd # StringDigit: 789123456
print(type(sd), sd)
sd = sd + "12f"