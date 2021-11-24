class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def binaryTreeToBST(self, root):
        out = []
        self.inorderTraversalGet(root, out)
        out.sort()
        self.inorderTraversalPut(root, out)

    def inorderTraversalGet(self, root, out):
        if (root):
            self.inorderTraversalGet(root.left, out)
            out.append(root.data)
            self.inorderTraversalGet(root.right, out)

    def inorderTraversalPut(self, root, out):
        if (root):
            self.inorderTraversalPut(root.left, out)
            root.data = out.pop(0)
            self.inorderTraversalPut(root.right, out)


if __name__ == '__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    sol = Solution()
    sol.binaryTreeToBST(root)
    out = []
    sol.inorderTraversalGet(root, out)
    print(out)
