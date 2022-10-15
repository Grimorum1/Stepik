class ObjList:

    def __init__(self, data, prev=None, next=None):
            self.__data = data
            self.__prev = prev
            self.__next = next

    def __str__(self):
        return self.__data


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.head == None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        x = self.head
        if indx > 0:
            for i in range(indx):
                x = x.next
            if x != self.tail:
                old = x.prev
                new = x.next
                old.next = new
                new.prev = old

            else:
                old = x.prev
                old.next = None
                self.tail = old
        else:
            if self.head == self.tail:
                self.head, self.tail = None, None
            else:
                self.head = x.next
                self.head.prev = None

    def __len__(self):
        counter = 1
        old = self.head
        new = self.tail
        while old != new:
            old = old.next
            counter += 1
        return counter

    def __call__(self, indx):
        old = self.head
        while indx!=0:
            indx -=1
            old = old.next
        else:
            return old.data

ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.remove_obj(0)
print(ln.head)
# ln.remove_obj(2)
# assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
# ln.add_obj(ObjList("Python"))
# assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
# assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
# assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"
#
# n = 0
# h = ln.head
#
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__next
#     n += 1
#
# assert n == 3, "при перемещении по списку через __next не все объекты перебрались"
#
# n = 0
# h = ln.tail
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__prev
#     n += 1
#
# assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"