class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        spisok = func
        def wrapper(*args, **kwargs):
            return [self.render(i) for i in spisok().split()]

        return wrapper


class RenderDigit:
    def __call__(self, string):
        try:
            return int(string)
        except ValueError:
            return None



render = RenderDigit()

@InputValues(render)
def input_dg():
    return input()

res = input_dg()
print(res)