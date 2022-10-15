class StackObj:
    counter = 0

    def __str__(self):
        return f"Объект №{self.link()}"



    @classmethod
    def link(cls):
        cls.counter += 1
        return cls.counter

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next==None:
            self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top==None:
            self.top = obj
        else:
            c = self.top
            while True:
                if c.next==None:
                    c.next = obj
                    break
                else:
                    c = c.next


    def pop(self):
        old = self.top
        new_obj = self.top.next
        while True:
            if new_obj!=None:
                if new_obj.next==None:
                    old.next = None
                    break
                old = new_obj
                new_obj = new_obj.next

            else:
                self.top = None
                break


    def get_data(self):
        c = self.top
        res = []
        if c != None:
            res = [c.data]
            while c.next!=None:
                c = c.next
                res.append(c.data)
        return res


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"