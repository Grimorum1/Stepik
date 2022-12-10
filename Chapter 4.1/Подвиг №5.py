class Thing:
    counter = 0

    def __init__(self, name, price, memory=None, frm=None, weight=None, dims=None):
        self.name = name
        self.price = price
        self.memory = memory
        self.frm = frm
        self.weight = weight
        self.dims = dims
        self.id = Thing.get_counter()

    @classmethod
    def get_counter(cls):
        Thing.counter += 1
        return Thing.counter

    def get_data(self):
        return (self.id, self.name, self.price, self.memory, self.frm, self.weight, self.dims)


class Table(Thing):

    def __init__(self, name, price, weight, dims):
        super().__init__(name, price, weight=weight, dims=dims)


class ElBook(Thing):

    def __init__(self, name, price, memory, frm):
        super().__init__(name, price, memory=memory, frm=frm)




table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())