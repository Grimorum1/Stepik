from random import randint


# здесь объявляйте класс RandomPassword
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        x = randint(self.min_length, self.max_length)
        dlina = len(self.psw_chars)
        res = ""
        for i in range(x):
            res += self.psw_chars[randint(0, dlina-1)]
        return res


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for i in range(3)]
print(lst_pass)