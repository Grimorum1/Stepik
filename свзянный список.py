class LinkedList:

    def __init__(self):
        self.tail = None
        self.head = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if self.head==None:
            self.head = obj


    def remove_obj(self):
        if self.tail!=None:
            self.tail = self.tail.get_prev()
        self.head = None

    def get_data(self):
        c = self.head
        res = [c.get_data()]
        while c.get_next() != None:
            c = c.get_next()
            res.append(c.get_data())
        return res


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))
res = ls.get_data()
print(ls.tail.get_data())
#print(res)
ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
ls_one.remove_obj()
print(ls_one.head)

