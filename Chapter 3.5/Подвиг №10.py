class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return (self.name.lower() == other.name.lower() and self.mass == other.mass)


class Box:
    def __init__(self):
        self.spisok = []

    def add_thing(self, obj):
        self.spisok.append(obj)

    def get_things(self):
        return self.spisok

    def __eq__(self, other):
        x = set(i.name for i in self.spisok)
        y = set(i.name for i in other.spisok)
        return x == y


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
mel = Thing('мел', 100)
mel1 = Thing('мел', 100)
print(mel==mel1)