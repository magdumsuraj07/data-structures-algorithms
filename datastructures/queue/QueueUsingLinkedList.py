# Following is the structure of the node class for a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def getSize(self):
        '''
        Returns number of elements present in queue.
        '''
        return self.__count

    def isEmpty(self):
        '''
        Returns True if queue is empty, otherwise returns False
        '''
        return self.__count == 0

    def enqueue(self, data):
        '''
        Insert new element in a queue.
        '''
        newNode = Node(data)
        if (self.__head is None):
            # Queue is empty
            self.__head = newNode
            self.__tail = newNode
        else:
            # Queue is not empty
            self.__tail.next = newNode
            self.__tail = newNode
        self.__count += 1

    def dequeue(self):
        '''
        Remove element from front of queue.
        '''
        if (self.isEmpty()):
            return -1
        else:
            ele = self.__head.data
            self.__head = self.__head.next
            self.__count -= 1
            return ele

    def front(self):
        '''
        Returns element at front of queue
        '''
        if (self.isEmpty()):
            return -1
        return self.__head.data
