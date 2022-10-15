class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.spisok = [cell(0) for _ in range(max_length)]

    def __getitem__(self, item):
        if not isinstance(item, int) or self.max_length<=item<0:
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.spisok[item].value

    def __setitem__(self, key, value):
        if not isinstance(key, int) or self.max_length<=key<0:
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.spisok[key].value = value


    def __str__(self):
        res = [str(i.value) for i in self.spisok]
        return "".join(res)



class Integer:

    def __init__(self, start_value=0):
        self.__start_value = start_value



    @property
    def value(self):
        return self.__start_value

    @value.setter
    def value(self, item):
        if not isinstance(item, int):
            raise ValueError('должно быть целое число')
        self.__start_value = item


ar_int = Array(10, cell=Integer)
print(ar_int[3])
ar_int[3] = 3
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
#print(ar_int)