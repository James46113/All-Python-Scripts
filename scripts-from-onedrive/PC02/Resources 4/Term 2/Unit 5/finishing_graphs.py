class Graph:
    def __init__(self, nodes: [(float, float)]):
        self.__nodes = nodes
        self.__adjacency_matrix = []
        for row in range(len(self.__nodes)):
            matrix_row = []
            for column in range(len(self.__nodes)):
                matrix_row.append(0)
            self.__adjacency_matrix.append(matrix_row)
