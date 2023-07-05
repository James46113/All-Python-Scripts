from random import randint
from time import sleep


class Queue:
    def __init__(self, *items):
        self.queue = []
        for item in items:
            self.queue.append(item)

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def add(self, value):
        self.queue.append(value)

    def ret(self):
        for x in self.queue:
            print(x)


def rec():
    recipe = Queue()
    count = 1
    while True:
        line = input('Enter next step: ')
        if line == "quit":
            break
        recipe.add(f"{count}. {line}")
        count += 1
    recipe.ret()


q = Queue("{}.{}.{}.{}".format(randint(0, 256), randint(0, 256), randint(0, 256), randint(0, 256)),
          "{}.{}.{}.{}".format(randint(0, 256), randint(0, 256), randint(0, 256), randint(0, 256)),
          "{}.{}.{}.{}".format(randint(0, 256), randint(0, 256), randint(0, 256), randint(0, 256)))

for _ in range(3):
    sleep(0.75)
    print(f"{q.get()} can enter website")

