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