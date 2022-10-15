class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst



    def __iter__(self):
        self.counter = 1
        self.res = []
        for i in self.lst:
            self.res += i[:self.counter]
            self.counter+=1
        return iter(self.res)



lst = [["00", "01", "02"],
       ["10", "11", "12", "13"],
       ["20", '21', '22'],
       ['30', '31', '32', '33'],
       ['40', '41', '42', '43', '44']
      ]
it = TriangleListIterator(lst)
it_iter = iter(it)
x = next(it_iter)
y = next(it_iter)
print(x, y)