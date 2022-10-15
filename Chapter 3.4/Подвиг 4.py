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
