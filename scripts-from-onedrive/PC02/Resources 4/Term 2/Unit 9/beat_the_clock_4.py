class Tree:
    def __init__(self, value):
        self.__value = value
        self.__children = []

    def add_child(self, child: "Tree") -> None:
        self.__children.append(child)

    def depth_first_search(self, target):
        if self.__value == target:
            return True

        # Check children here

