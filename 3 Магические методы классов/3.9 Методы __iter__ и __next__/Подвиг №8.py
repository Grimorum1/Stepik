"""
Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:

Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)

где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

"""

class Stack:

    def __init__(self, top=None):
        self.top = top
        self.spisok = []



    def push_back(self, obj):
        self.spisok.insert(-1, obj)
        if self.top==None:
            self.top=obj
        else:
            old = self.top
            new = self.top.next
            while new!=None:
                old = new
                new = new.next
            else:
                old.next = obj


    def push_front(self, obj):
        self.spisok.insert(0, obj)
        if self.top==None:
            self.top=obj
        else:
            obj.next = self.top
            self.top = obj


    def __getitem__(self, item):
        if 0<=item<len(self.spisok):
            return self.spisok[item].data
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if 0 <= key < (len(self.spisok)-1):
            top = self.top
            while top.data!=self.spisok[key].data:
                top = top.next
            else:
                top.data = value
        else:
            raise IndexError('неверный индекс')

    def __len__(self):
        return len(self.spisok)

    def __iter__(self):
        return iter(self.spisok)



class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))


assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"