"""
Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]

Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка, как это показано в примере:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен сохраняться)

Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями

Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]

Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

lst = res_2.get_list() # [1, 2, 3]

P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.

"""

class NewList:
    def __init__(self, lst=None):
        self.lst = lst if lst!=None else []


    def __sub__(self, other):
        if isinstance(other, NewList):
            other = other.lst

        other = [(i, type(i)) for i in other[:]]
        res = []
        for i in self.lst:
            if (i, type(i)) in other:
                other.remove((i, type(i)))
                continue
            res.append(i)
        return NewList(res)



    def __isub__(self, other):
        if isinstance(other, NewList):
            other = other.lst

        other = [(i, type(i)) for i in other[:]]
        res = []
        for i in self.lst:
            if (i, type(i)) in other:
                other.remove((i, type(i)))
                continue
            res.append(i)
        self.lst = res
        return self


    def __rsub__(self, other):
        #print(other)
        return NewList(other) - self

    def get_list(self):
        return [i for i in self.lst]




lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])
assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"
res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
