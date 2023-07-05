class Stack:
    def __init__(self, *args):
        self.queue = []
        for item in args: self.queue.append(item)

    def push(self, item):  # Add item to list
        self.queue.append(item)

    def pop(self):  # Take away item from list
        if len(self.queue) > 0:
            return self.queue.pop(-1)

    def __str__(self):
        ret = []
        for x in range(len(self.queue)-1, -1, -1):
            ret.append(self.queue[x])
        return str(ret)


s = Stack("Documents.txt", "Names.txt", "Cars.txt", "Flights.txt", "Finances.txt")
print(s)
for x in range(1, 6):
    with open(s.pop(), "w") as f:
        f.write(f"Document {x}\nName: {input('Enter your name: ')}")
