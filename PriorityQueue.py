import Queue

class PriorityQueue(Queue.PriorityQueue):
    def peek(self):
        v = self.get()
        self.put(v)
        return v

    def remove(self, value):
        values = []
        while not self.empty():
            v = self.get()
            if v != value:
                values.append(v)

        for v in values:
            self.put(v)

