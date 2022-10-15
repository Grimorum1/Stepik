class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if x1 and x2 and y1 and y2:
            self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2


    def __bool__(self):
        if len(self.__dict__)>0:
            if not bool(self.x1):
                return False
            if not bool(self.x2):
                return False
            if not bool(self.y2):
                return False
            if not bool(self.y1):
                return False
            return True
        return False

    def get_coords(self):
        if bool(self):
            return (self.x1, self.y1, self.x2, self.y2)
        raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 4, 4), Ellipse(1, 1, 5, 5)]
for i in lst_geom:
    if bool(i):
        i.get_coords()
