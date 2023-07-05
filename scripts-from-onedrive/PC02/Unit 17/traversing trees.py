class Tree:
    def __init__(self, value: int):
        self.__children = []
        self.__value = value

    def add_child(self, child: "Tree") -> None:
        self.__children.append(child)

    def dfs(self, target):
        if self.__value == target:
            return self
        for child in self.__children:
            res = child.dfs(target)
            print(child.__value)
            if res is not None:
                return res

    def bfs(self, target):
        visited = []
        found = [self]
        while len(found) > 0:
            t = found.pop(0)
            print(t.__value)
            if t.__value == target:
                return t
            for child in t.__children:
                if child not in found and child not in visited:
                    found.append(child)
            visited.append(t)

    def __str__(self) -> str:
        if len(self.__children) == 0:
            return "Leaf"
        return "Parent"


r = Tree(34)
t1 = Tree(15)
t2 = Tree(46)
r.add_child(t1)
r.add_child(t2)
res = r.bfs(46)
print(res)
