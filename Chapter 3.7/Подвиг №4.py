class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return bool(self.score)


# считывание списка из входного потока (эту строчку и список lst_in не менять)
lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']
players_filtered = list(filter(bool, [Player(*i.split(";")) for i in lst_in]))
