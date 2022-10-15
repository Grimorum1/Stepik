class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, top=None):
        self.top = top
        self.count = 0

    def push(self, obj):
        self.count +=1
        if self.top==None:
            self.top = obj
        else:
            old = self.top
            new = self.top.next
            while new!=None:
                old = new
                new = new.next
            else:
                old.next = obj

    def pop(self):
        self.count-=1
        if self.count==0:
            res = self.top
            self.top = None
            return res
        else:
            old = self.top
            new = old.next
            new2 = new.next
            while new2!=None:
                old = new
                new = new2
                new2 = new.next
            else:
                res = new
                old.next = None
                return res

    def __getitem__(self, item):
        if item>(self.count-1) or type(item)!=int or 0>item:
            raise IndexError('неверный индекс')
        new = self.top
        while item!=0:
            new = new.next
            item -=1
        else:
            return new

    def __setitem__(self, key, value):
        if key > (self.count - 1) or type(key) != int or 0 > key:
            raise IndexError('неверный индекс')

        if key==0:
            new = self.top.next
            self.top = value
            self.top.next = new
        else:
            old = self.poisk(key-1)
            new = self.poisk(key+1)
            old.next = value
            value.next = new


    def poisk(self, value):
        old = self.top
        while value!=0:
            value -=1
            old = old.next
        else:
            return old


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"


try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

