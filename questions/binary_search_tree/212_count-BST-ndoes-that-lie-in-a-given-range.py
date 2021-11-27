class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getCount(root, low, high):
    count = [0]
    getCountUtil(root, low, high, count)
    return count[0]


def getCountUtil(root, low, high, count):
    if (root):
        getCountUtil(root.left, low, high, count)
        if (root.data >= low and root.data <= high):
            count[0] += 1
        getCountUtil(root.right, low, high, count)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)
    print(getCount(root, 5, 45))
