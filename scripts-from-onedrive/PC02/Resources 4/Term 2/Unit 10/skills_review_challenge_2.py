class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop(-1)


stack = Stack()
stack.push("Bob")
stack.push("is")
stack.push("name")
stack.push("my")
stack.push("hello")
for _ in range(5): print(stack.pop())
