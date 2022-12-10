"""
Подвиг 6. Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по цепочке до последнего:

СМОТРИ КАРТИНКУ StackObj

Для этого в программе объявлялись два класса: 

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:

obj = StackObj(data)

где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса StackObj должен иметь следующие локальные атрибуты:

data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта стек-подобной структуры

В каждом объекте класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый объект стека (если стек пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец стека;
pop(self) - извлечение последнего объекта с его удалением из стека;

Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:

obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый

Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:

raise IndexError('неверный индекс')

Пример использования классов Stack и StackObj (эти строчки в программе не писать):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""

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

