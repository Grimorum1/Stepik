class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        for i in args:
            if i.split(".")[-1] in self.extensions:
                return True
            return False




fs = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]


acceptor = ImageFileAcceptor(("jpeg", "html"))
res = filter(acceptor, fs)
print(set(res))
assert set(res) == set(["forest.jpeg", "my.html"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"
