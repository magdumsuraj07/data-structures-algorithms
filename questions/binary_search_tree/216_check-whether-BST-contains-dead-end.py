import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isdeadEnd(root):
    return deadEndUtil(root, 1, sys.maxsize)


def deadEndUtil(root, Min, Max):
    if root is None:
        return False

    if Min == Max:
        return True

    return (deadEndUtil(root.left, Min, root.data - 1) or
            deadEndUtil(root.right, root.data + 1, Max))


if __name__ == '__main__':
    #     8
    #    /  \
    #   7    10
    #  /    /  \
    # 2    9    13

    root = Node(10)
    root.left = Node(7)
    root.right = Node(10)
    root.left.left = Node(2)
    root.right.left = Node(9)
    root.right.right = Node(13)
    print(isdeadEnd(root))
