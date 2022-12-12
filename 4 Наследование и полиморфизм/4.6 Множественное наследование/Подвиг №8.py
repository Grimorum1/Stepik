class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if request["method"].upper() not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        return self.__getattribute__(request['method'].lower())(request)



class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html)