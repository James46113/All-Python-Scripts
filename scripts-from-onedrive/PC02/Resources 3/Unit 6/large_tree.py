import random


class Tree:
    def __init__(self, value: int):
        self.__children = []
        self.__value = value

    def add_child(self, child: "Tree") -> None:
        self.__children.append(child)

    def __str__(self) -> str:
        return "Parent" if len(self.__children) > 0 else "Leaf"

    def dfs(self, target):
        # Copy your Depth First Search code into this function
        pass

    def bfs(self, target):
        # Copy your Breadth First Search code into this function
        pass


def create_tree(list_of_numbers: [int]) -> Tree:
    if len(list_of_numbers) == 0:
        pass
    elif len(list_of_numbers) == 1:
        return Tree(list_of_numbers[0])
    else:
        mid = int(len(list_of_numbers) // 2)
        root = Tree(list_of_numbers[mid])
        left_half = list_of_numbers[:mid]
        right_half = list_of_numbers[mid + 1:]
        left_result = create_tree(left_half)
        if left_result is not None:
            root.add_child(left_result)
        right_result = create_tree(right_half)
        if right_result is not None:
            root.add_child(right_result)
        return root


numbers = []
for count in range(10000):  # Can change the number of nodes created here
    numbers.append(random.randint(0, 1000))
numbers.sort()
my_tree = create_tree(numbers)
my_tree.bfs(1500)
