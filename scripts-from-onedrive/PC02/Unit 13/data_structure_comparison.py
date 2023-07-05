from random import randint


class Stack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            if isinstance(item, list):
                for item2 in item:
                    self.stack.append(item2)
            else:
                self.stack.append(item)

    def add(self, item):  # Add item to list
        self.stack.append(item)

    def get(self):  # Take away item from list
        if len(self.stack) > 0:
            return self.stack.pop(-1)

    def __str__(self):
        ret = []
        for x in range(len(self.stack)-1, -1, -1):
            ret.append(self.stack[x])
        return str(ret)


class Queue:
    def __init__(self, *items):
        self.queue = []
        for item in items:
            if isinstance(item, list):
                for item2 in item:
                    self.queue.append(item2)
            else:
                self.queue.append(item)

    def add(self, value):
        self.queue.append(value)

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)


mylist = [randint(0, 256) for _ in range(20)]

q = Queue(mylist)
s = Stack(mylist)

print(q)
print(s)

for x in range(20):
    print(q.get())
    print(s.get())
