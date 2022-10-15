class Handler:
    def __init__(self, methods):
        self.methods = methods
        #print(self.methods)

    def get(self, func, request, *args, **kwargs):
        if "GET" in self.methods:
            return f"GET: {func(request)}"
        return None

    def post(self, func, request, *args, **kwargs):
        if "POST" in self.methods:
            return f"POST: {func(request)}"
        return None


    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            m = request.get("method")
            if m:
                if m=="GET":
                    return self.get(func, request)
                elif m=="POST":
                    return self.post(func, request)
                else:
                    return None
            else:
                return self.get(func, request)
        return wrapper




assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"

@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"

assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"

@Handler(methods=('POST'))
def index(request):
    return "index"

assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"