class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def toSumTree(root):
    # Base case
    if (root is None):
        return 0

    # Store the old value
    old_val = root.data

    root.data = toSumTree(root.left) + toSumTree(root.right)

    return root.data + old_val


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)

    toSumTree(root)
