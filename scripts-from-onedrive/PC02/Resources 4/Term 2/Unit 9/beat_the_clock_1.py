class Queue:
    def __init__(self):
        self.__data = []

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)
