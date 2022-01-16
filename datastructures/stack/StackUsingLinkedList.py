# Following is the structure of the node class for a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    '''
    Stack implementation using singly linked list.
    '''
    def __init__(self):
        self.__head = None
        self.__count = 0

    def getSize(self):
        '''
        Returns number of elements existing in stack.
        '''
        return self.__count

    def isEmpty(self):
        '''
        Returns True if stack is empty, otherwise returns False
        '''
        return self.getSize() == 0

    def push(self, data):
        '''
        Push an element to stack.
        '''
        temp = Node(data)
        temp.next = self.__head
        self.__head = temp
        self.__count += 1

    def pop(self):
        '''
        Pops elements from stack.
        '''
        if (self.getSize() > 0):
            temp = self.__head
            self.__head = self.__head.next
            self.__count -= 1
            return temp.data
        else:
            return -1

    def top(self):
        '''
        Returns element at top of stack.
        '''
        if (self.getSize() > 0):
            return self.__head.data
        else:
            return -1
