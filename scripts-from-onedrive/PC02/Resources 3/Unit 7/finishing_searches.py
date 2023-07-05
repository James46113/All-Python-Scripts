class Tree:
    def __init__(self, value: int):
        self.__children = []
        self.__value = value

    def add_child(self, child: "Tree") -> None:
        self.__children.append(child)

    def __str__(self) -> str:
        return "Parent" if len(self.__children) > 0 else "Leaf"

    def depth_first_search(self, target):
        print("Current Node Value: {}".format(self.__value))
        if self.__value == target:
            return self
        # Finish from here

    def breadth_first_search(self, target):
        visited = []
        found = [self]
        while len(found) > 0:
            current = found.pop(0)
            visited.append(current)
            print("Current Node Value: {}".format(current.__value))
            # Finish from here
