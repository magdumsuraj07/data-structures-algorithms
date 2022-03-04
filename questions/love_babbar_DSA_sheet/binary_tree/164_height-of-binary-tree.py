class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def height(root):
    if (root is None):
        return 0

    lHeight = height(root.left)
    rHeight = height(root.right)

    return 1 + max(lHeight, rHeight)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(3)
    print(height(root))
