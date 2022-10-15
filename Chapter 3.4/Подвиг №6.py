class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None


    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def data(self):
        return self.__data


class Stack:
    def __init__(self, top=None):
        self.top = top


    def push_back(self, obj): # добавление объекта класса StackObj в конец односвязного списка;
        if self.top==None:
            self.top = obj
        else:
            x = self.top
            while x.next!=None:
                x = x.next
            else:
                x.next = obj


    def pop_back(self): # удаление последнего объекта из односвязного списка.
        old = self.top
        new = old.next
        while new!= None:
            old = new
            new = new.next
        else:
            old = None


    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self

    def __imul__(self, other):
        return self * other



assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"