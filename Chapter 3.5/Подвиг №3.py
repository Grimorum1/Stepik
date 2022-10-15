class Track:
    def __init__(self, start_x, start_y):
        self.__start_x = start_x
        self.__start_y = start_y
        self.__spisok = [(start_x, start_y)]

#                   ((x1 - x0)**2 + (y1 - y0)**2) ** 0.5
    def __len__(self):
        return

    def __eq__(self, other):
        return

    def add_track(self, tr):
        pass


    def get_tracks(self):
        pass


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

