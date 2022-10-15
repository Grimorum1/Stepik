class PolyLine:
    def __init__(self, *args):
        self.spisok = [*args]

    def add_coord(self, x, y):
        self.spisok.append((x, y))

    def remove_coord(self, indx):
        self.spisok.pop(indx)

    def get_coords(self):
        return tuple(self.spisok)
