class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def LCA(root, n1, n2):
    while (root):
        if (root.data < n1 and root.data < n2):
            root = root.right
        elif (root.data > n1 and root.data > n2):
            root = root.left
        else:
            return root


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    node = LCA(root, 6, 7)
    print(node.data)
