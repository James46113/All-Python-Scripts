class Queue:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
for _ in range(5): print(q.pop())
