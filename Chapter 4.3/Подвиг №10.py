class ItemAttrs:

    def __getitem__(self, item):
        if item==0:
            return self.__dict__["x"]
        return self.__dict__["y"]

    def __setitem__(self, key, value):
        if key == 0:
            self.__dict__["x"] = value
        else:
            self.__dict__["y"] = value



class Point(ItemAttrs):

    def __init__(self, x, y):
        self.x = x
        self.y = y




pt = Point(1, 2.5)
x = pt[0]
print(x)# 1
y = pt[1]
print(y)# 2.5
pt[0] = 10
print(pt.x)