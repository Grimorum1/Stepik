class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None


    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        res = root
        for i in x:

            if i == 1:
                res = res.left
                if x[1]==1:
                    res = res.left
                    break
                else:
                    res = res.right
                    break
            else:
                res = res.right
                if x[2]==1:
                    res = res.left
                    break
                else:
                    res = res.right
                    break

        return res.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node != None:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree, 'predict'), "в классе DecisionTree должны быть методы add_obj и predict"

assert type(TreeObj.left) == property and type(TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

print(DecisionTree.predict(root, [0, 1, 0]))
assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"

