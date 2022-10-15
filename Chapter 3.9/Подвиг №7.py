class IterColumn:

    def __init__(self, lst, column):
        self.lst = lst
        self.column = column


    def __iter__(self):
        self.res = [i[self.column] for i in self.lst]
        return iter(self.res)