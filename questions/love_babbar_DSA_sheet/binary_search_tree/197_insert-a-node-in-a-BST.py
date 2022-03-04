class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorderPrint(root):
    if (root):
        inorderPrint(root.left)
        print(root.data)
        inorderPrint(root.right)


def insert(root, Key):
    if (root is None):
        return Node(Key)
    else:
        if (Key == root.data):
            return root
        elif (Key > root.data):
            root.right = insert(root.right, Key)
        elif (Key < root.data):
            root.left = insert(root.left, Key)
    return root


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    inorderPrint(root)
    root = insert(root, 4)
    inorderPrint(root)
