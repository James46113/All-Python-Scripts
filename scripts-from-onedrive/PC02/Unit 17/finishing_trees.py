class Tree:
    def __init__(self, value: int):
        self.__children = []
        self.__value = value

    def add_child(self, child: "Tree") -> None:
        self.__children.append(child)

    def __str__(self):
        if len(self.__children) == 0:
            return "Leaf"
        return "Parent"
