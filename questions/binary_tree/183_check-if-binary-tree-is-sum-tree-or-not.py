class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def isSumTree(self, root):
        if (root is None):
            return True
        if (root.left is None and root.right is None):
            return True

        leftSubtreeSum = self.add(root.left)
        rightSubtreeSum = self.add(root.right)

        if (root.data == leftSubtreeSum + rightSubtreeSum
           and self.isSumTree(root.left)
           and self.isSumTree(root.right)):
            return True
        else:
            return False

    def add(self, root):
        if (root is None):
            return 0
        if (root.left is None and root.right is None):
            return root.data

        leftSum = self.add(root.left)
        rightSum = self.add(root.right)

        return leftSum + rightSum + root.data


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(10)
    root.left.right = Node(10)

    sol = Solution()
    print(sol.isSumTree(root))
