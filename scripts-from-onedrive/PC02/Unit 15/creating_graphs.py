"""
class Graph:
    def __init__(self, nodes_l: list):
        self.__nodes = nodes_l
        self.__adjacency_matrix = []

        if len(self.__nodes) != 0:
            for _ in self.__nodes:
                self.__matrix_row = []
                for _ in self.__nodes:
                    self.__matrix_row.append(0)
                self.__adjacency_matrix.append(self.__matrix_row)
            print(self.__adjacency_matrix)
        else:
            print("nodes list empty")

    def add_edge(self, node1: int, node2: int):
        try:
            self.__adjacency_matrix[node1][node2] = 1
            self.__adjacency_matrix[node2][node1] = 1
            for line in self.__adjacency_matrix:
                print(line)
        except Exception:
            print("Integers too large")

    def __str__(self) -> str:
        self.__ret = ""
        for ind, item in enumerate(self.__nodes):
            if ind < len(self.__nodes) - 1:
                self.__ret += str(item) + ", "
            else:
                self.__ret += str(item)
        return self.__ret


tuples = [(50, 0),
         (0, 50),
         (100, 50)]

g = Graph(tuples)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
print(g)
"""
import tkinter


class Graph:
    def __init__(self, nodes_l: list):
        self.__nodes = nodes_l
        self.__adjacency_matrix = []

        if len(self.__nodes) != 0:
            for _ in self.__nodes:
                self.__matrix_row = []
                for _ in self.__nodes:
                    self.__matrix_row.append(0)
                self.__adjacency_matrix.append(self.__matrix_row)
            print(self.__adjacency_matrix)
        else:
            print("nodes list empty")

    def add_edge(self, node1: int, node2: int):
        try:
            self.__adjacency_matrix[node1][node2] = 1
            self.__adjacency_matrix[node2][node1] = 1
            for line in self.__adjacency_matrix:
                print(line)
        except Exception:
            print("Integers too large")

    def __str__(self) -> str:
        self.__ret = ""
        for ind, item in enumerate(self.__nodes):
            if ind < len(self.__nodes) - 1:
                self.__ret += str(item) + ", "
            else:
                self.__ret += str(item)
        return self.__ret

    def draw_graph(self, graph_width: int, graph_height: int) -> None:
        window = tkinter.Tk()
        window.title("Drawing Graphs")
        canvas = tkinter.Canvas(window, width=graph_width, height=graph_height, bg="white")
        canvas.pack()
        for row_index in range(len(self.__adjacency_matrix)):
            for col_index in range(len(self.__adjacency_matrix[row_index])):
                if self.__adjacency_matrix[row_index][col_index] == 1:
                    node1 = self.__nodes[row_index]
                    node2 = self.__nodes[col_index]
                    canvas.create_line(node1, node2)
        for node in self.__nodes:
            canvas.create_oval(node[0] - 5, node[1] - 5, node[0] + 5, node[1] + 5, fill="red")

        canvas.mainloop()


tuples = [(100, 100),
         (150, 100),
          (175, 150),
          (150, 195),
          (100, 195),
          (70, 145)]

# Create Graph object here
g = Graph(tuples)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 0)
print(g)

g.draw_graph(500, 500)  # Change GRAPH_NAME_HERE to Graph object (and choose a size for the window)
