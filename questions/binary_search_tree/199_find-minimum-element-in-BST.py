class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minvalue(root):
    curr = root
    while (curr.left is not None):
        curr = curr.left
    return curr.data


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.right = Node(7)
    root.left.left.left = Node(1)

    print(minvalue(root))
