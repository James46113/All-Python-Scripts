class Tree:
    def __init__(self, value):
        self.__children = []
        self.__value = value

    def add_child(self, child: "Tree"):
        self.__children.append(child)


t1 = Tree(20)
t2 = Tree(18)
t3 = Tree(12)
t4 = Tree(15)
t5 = Tree(17)

t5.add_child(t4)
t5.add_child(t2)
t4.add_child(t3)
t2.add_child(t1)