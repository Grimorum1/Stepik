from math import sqrt


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        dlina = ((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)
        dlina = int(sqrt(dlina))
        return dlina


line = Line(1, 1, 4, 4)
print(bool(line))