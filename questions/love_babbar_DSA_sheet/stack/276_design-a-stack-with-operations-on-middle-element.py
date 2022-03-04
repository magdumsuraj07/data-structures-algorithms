class DLLNode:
    '''
    This class represents Doubly Linked List Node
    '''
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CustomStack:
    '''
    This class represents custom stack implementation using DLL
    '''
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

    def push(self, value):
        node = DLLNode(value)
        if (self.head):
            node.next = self.head
            self.head.prev = node
        self.head = node

        self.count += 1

        if (self.mid is None):
            self.mid = self.head
        else:
            if (self.count % 2 != 0):
                self.mid = self.mid.prev

    def pop(self):
        if (self.count == 0):
            print("Stack is empty")
            return -1

        returnVal = self.head.data
        self.head = self.head.next
        if (self.head is not None):
            self.head.prev = None
        self.count -= 1

        if (self.count % 2 == 0):
            self.mid = self.mid.next

        return returnVal

    def findMiddle(self):
        if (self.count == 0):
            print("Stack is empty")
            return -1
        return self.mid.data


if __name__ == '__main__':
    myStack = CustomStack()
    myStack.push(1)
    print(myStack.findMiddle())
    myStack.push(2)
    myStack.push(3)
    print(myStack.findMiddle())
    myStack.push(4)
    myStack.pop()
    print(myStack.findMiddle())
