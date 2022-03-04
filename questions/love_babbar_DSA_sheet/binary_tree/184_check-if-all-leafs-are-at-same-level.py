class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.leafLevel = 0

    def check(self, root):
        currLevel = 0
        return self.checkUtil(root, currLevel)

    def checkUtil(self, root, currLevel):
        if (root is None):
            return True

        if (root.left is None and root.right is None):
            if (self.leafLevel == 0):
                self.leafLevel = currLevel
                return True

            return self.leafLevel == currLevel

        return self.checkUtil(root.left, currLevel+1) and \
            self.checkUtil(root.right, currLevel+1)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(10)
    root.left.right = Node(15)

    sol = Solution()
    print(sol.check(root))
