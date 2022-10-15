import time
class GeyserClassic:
    MAX_DATE_FILTER = 100
    FILTRES = {1: None, 2: None, 3: None}
    def add_filter(self, slot_num, filter):
        if slot_num==1 and isinstance(filter, Mechanical) and self.FILTRES[1]==None:
            self.FILTRES[1] = filter
        elif slot_num==2 and isinstance(filter, Aragon) and self.FILTRES[2] == None:
            self.FILTRES[2] = filter
        elif slot_num==3 and isinstance(filter, Calcium) and self.FILTRES[3] == None:
            self.FILTRES[3] = filter

    def remove_filter(self, slot_num):
        self.FILTRES[slot_num]=None

    def get_filters(self):
        return (self.FILTRES[1], self.FILTRES[2], self.FILTRES[3])

    def water_on(self):

        if self.FILTRES[1]==None or self.FILTRES[2]==None or self.FILTRES[3]==None:
            return False
        for i in self.FILTRES:
            f = self.FILTRES[i]
            if (time.time() - f.date) >= self.MAX_DATE_FILTER:
                return False
        return True




class Mechanical:

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__.keys():
            return
        object.__setattr__(self, key, value)


class Aragon:

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__.keys():
            return
        object.__setattr__(self, key, value)

class Calcium:

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__.keys():
            return
        object.__setattr__(self, key, value)


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"