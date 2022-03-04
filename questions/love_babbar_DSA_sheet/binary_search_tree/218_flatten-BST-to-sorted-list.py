class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorderTraverse(root):
    if (root is None):
        return
    global prev
    inorderTraverse(root.left)
    prev.left = None
    prev.right = root
    prev = root
    inorderTraverse(root.right)


def inorderPrint(root):
    if (root):
        inorderPrint(root.left)
        print(root.data, end=" ")
        inorderPrint(root.right)


def flattenBST(root):
    dummy = Node(-1)
    global prev
    prev = dummy
    inorderTraverse(root)
    prev.left = None
    prev.right = None
    return dummy.right


if __name__ == '__main__':
    #     8
    #    /  \
    #   7    10
    #  /    /  \
    # 2    9    13

    root = Node(8)
    root.left = Node(7)
    root.right = Node(10)
    root.left.left = Node(2)
    root.right.left = Node(9)
    root.right.right = Node(13)

    prev = None
    flattenedRoot = flattenBST(root)
    inorderPrint(flattenedRoot)
