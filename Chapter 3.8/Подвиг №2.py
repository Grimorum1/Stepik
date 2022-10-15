class Record:
    def __init__(self, **kwargs):
        self.spisok = []
        for i, v in kwargs.items():
            self.__dict__[i] = v
            self.spisok.append(i)

    def __getitem__(self, item):
        if item>len(self.spisok):
            raise IndexError('неверный индекс поля')
        key = self.spisok[item]
        return key

    def __setitem__(self, key, value):
        item = self[key]
        self.__dict__[item] = value
        self.spisok[key]=value


r = Record(pk=1, title='Python ООП', author='Балакирев')
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError