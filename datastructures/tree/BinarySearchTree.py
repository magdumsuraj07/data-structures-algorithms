class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, val):
    if (root is None):
        return Node(val)
    else:
        if (root.data == val):
            return root
        elif (root.data < val):
            root.right = insert(root.right, val)
        else:
            root.left = insert(root.left, val)
    return root


def inorderPrint(root):
    if (root is None):
        return
    inorderPrint(root.left)
    print(root.data, end=" ")
    inorderPrint(root.right)


if __name__ == '__main__':
    root = Node(10)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 7)
    inorderPrint(root)
