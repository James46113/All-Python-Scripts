#  Complete queue from resources
class Queue:
    def __init__(self, *args):
        self.queue = []
        for item in args: self.queue.append(item)

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
