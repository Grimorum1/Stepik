"""
Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)

Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]

P.S. В программе на экран ничего выводить не нужно.

"""


# здесь объявляйте класс SingletonFive
class SingletonFive:
    counter = 0
    __inst = None

    def __new__(cls, *args, **kwargs):
        if cls.counter < 5:
            cls.counter += 1
            cls.__inst = super().__new__(cls)
            return cls.__inst
        return cls.__inst

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять




