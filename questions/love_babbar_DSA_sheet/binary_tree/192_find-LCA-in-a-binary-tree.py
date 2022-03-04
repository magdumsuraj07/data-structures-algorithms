class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def lca(self, root, n1, n2):
        if (root is None):
            return None

        if (root.data == n1 or root.data == n2):
            return root

        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)

        if (left and right):
            return root
        elif (left):
            return left
        else:
            return right


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    sol = Solution()
    node = sol.lca(root, 6, 7)
    print(node.data)
