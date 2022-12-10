

def class_log(vector_log):
    def integer_params(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, integer_params_decorated(v))

        return cls

    def integer_params_decorated(v):
        def wrapper(*args, **kwargs):
            vector_log.append(v.__name__)
            return v(*args, **kwargs)

        return wrapper
    return integer_params


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def get_coords(self):
        return self.__coords

v = Vector(1, 2, 3)
v[0] = 10
print(v[1])
v.get_coords()
print(vector_log)
print(v[0])