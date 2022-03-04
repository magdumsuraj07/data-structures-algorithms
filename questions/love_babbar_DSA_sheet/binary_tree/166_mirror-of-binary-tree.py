class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def inorderTraverse(root):
    if root:
        inorderTraverse(root.left)
        print(root.data, end=" ")
        inorderTraverse(root.right)


def mirror(root):
    if (root is None):
        return

    mirror(root.left)
    mirror(root.right)
    # Swap left and right nodes
    root.left, root.right = root.right, root.left


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)

    inorderTraverse(root)
    mirror(root)
    print()
    inorderTraverse(root)
