class Graph:
    def __init__(self, node_list):
        self.__nodes = node_list
        self.__matrix = []
        for _ in self.__nodes:
            temp = []
            for _ in self.__nodes:
                temp.append(0)
            self.__matrix.append(temp)

    def connect(self, node1: int, node2: int):
        try:
            self.__matrix[node1][node2] = 1
            self.__matrix[node2][node1] = 1
        except IndexError:
            pass


