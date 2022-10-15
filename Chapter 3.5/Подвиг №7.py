class FileAcceptor:
    def __init__(self, *args):
        self.files = [i for i in args]


    def __add__(self, other):
        res = self.files + other.files
        return FileAcceptor(*res)


    def __call__(self, file):
        if file.split(".")[-1] in self.files:
            return True
        return False




filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
filenames = list(filter(acceptor12, filenames))
print(filenames)