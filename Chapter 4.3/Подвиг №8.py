class SoftList(list):

    def __getitem__(self, item):
        if abs(item) > len(self)-1:
            return False
        return super().__getitem__(item)


sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False
print(sl[-7]) # False