class Tree:
    def __init__(self, value):
        self.__value = value
        self.__children = []

    def add_child(self, child: "Tree") -> None:
        self.__children.append(child)

    def breadth_first_search(self, target):
        visited = []
        found = [self]
        while len(found) > 0:
            current_node = found.pop(0)
            visited.append(current_node)
            if current_node.__value == target:
                return True

            # Check children here
