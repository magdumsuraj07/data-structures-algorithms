class CircularQueue:
    def __init__(self, _size):
        self.size = _size
        self.items = [None] * _size
        self.front = self.rear = -1

    def isEmpty(self):
        return self.rear == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if (self.isFull()):
            raise Exception("Queue is full")
        if (self.isEmpty()):
            self.front += 1
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = data

    def dequeue(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty")

        val = self.items[self.front]
        if (self.front == self.rear):
            self.front = self.rear = -1
        self.front = (self.front + 1) % self.size
        return val
