import tkinter


class Graph:
    # Insert __init__ and add_node functions here

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


# Create Graph object here

GRAPH_NAME_HERE.draw_graph(500, 500)  # Change GRAPH_NAME_HERE to Graph object (and choose a size for the window)
