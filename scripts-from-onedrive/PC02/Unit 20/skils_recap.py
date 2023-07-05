class PrinterQueue:
    def __init__(self, *args):
        self.__queue = []
        for item in args:
            self.__queue.append(item)

    def push(self, value):
        self.__queue.append(value)

    def pop(self):
        return self.__queue.pop(0)


q = PrinterQueue("a", "b", "c")
for x in range(3):
    with open(f"txt{x}.txt", "w") as f:
        f.write(q.pop())


class ActionStack:
    def __init__(self, *args):
        self.__queue = []
        for item in args:
            self.__queue.append(item)

    def push(self, value):
        self.__queue.append(value)

    def pop(self):
        return self.__queue.pop(-1)


q = ActionStack("make file3", "make file2", "make file1")
for _ in range(3): print(q.pop())


class LocationClass:
    def __init__(self, *args):
        self.__places = []
        for item in args: self.__places.append(item)
        self.__matrix = []
        for x in range(len(self.__places)):
            self.__temp = []
            for y in range(len(self.__places)):
                self.__temp.append(0)
            self.__matrix.append(self.__temp)
            print(x)

    def connect(self, node1, node2):
        self.__matrix[node1][node2] = 1
        self.__matrix[node2][node1] = 1

    def retplaces(self):
        return self.__places

    def retmatrix(self):
        return self.__matrix


lc = LocationClass((12, 65), (235, 52), (234, 354), (74, 134), (635, 345))
lc.connect(0, 1)
lc.connect(1, 2)
print(lc.retmatrix())
print(lc.retplaces())