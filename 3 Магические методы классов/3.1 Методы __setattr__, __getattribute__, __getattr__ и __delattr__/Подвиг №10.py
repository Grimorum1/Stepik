"""
Подвиг 10. Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно быть три слота для фильтров. Каждый слот строго для своего класса фильтра:

Mechanical - для очистки от крупных механических частиц;
Aragon - для последующей очистки воды;
Calcium - для обработки воды на третьем этапе.

СМОТРИ РИСУНОК GeyserClassic

Объекты классов фильтров должны создаваться командами:

filter_1 = Mechanical(дата установки)
filter_2 = Aragon(дата установки)
filter_3 = Calcium(дата установки)

Во всех объектах этих классов должен формироваться локальный атрибут:

date - дата установки фильтров (для простоты - положительное вещественное число).

Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение). В случае присвоения нового значения, прежнее значение не менять. Ошибок никаких не генерировать.

Объекты класса GeyserClassic должны создаваться командой:

g = GeyserClassic()

А сам класс иметь атрибут:

MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)

и следующие методы:

add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3), если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно установить только объекты класса Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.

remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);

get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);

water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.

Метод water_on() должен возвращать значение True при выполнении следующих условий:

- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])

Пример использования классов  (эти строчки в программе писать не нужно):

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно

P.S. На экран ничего выводить не нужно.

"""

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
