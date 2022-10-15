class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.stop = 5
        self.current = 0
        self.__index = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __getitem__(self, item):
        if 0 <= item <= 4:
            return self.__index[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if 0 <= key <= 4:
            self.__index[key] = value
        else:
            raise IndexError('неверный индекс')


    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            res = self.current
            self.current += 1
            return self.__index[res]
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers[0], pers[1], pers[2], pers[3], pers[4])