class Stack(object):
    """
    Stack class implementation using list.
    """
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)
