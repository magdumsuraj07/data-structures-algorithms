class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def sumOfLongRootToLeafPath(self, root):
        return self.sumOfLongRootToLeafPathUtil(root)[1]

    def sumOfLongRootToLeafPathUtil(self, root):
        if (root is None):
            return (0, 0)

        leftHeight, leftSum = self.sumOfLongRootToLeafPathUtil(root.left)
        rightHeight, rightSum = self.sumOfLongRootToLeafPathUtil(root.right)

        if (leftHeight > rightHeight):
            return (leftHeight + 1, leftSum + root.data)
        elif (rightHeight > leftHeight):
            return (rightHeight + 1, rightSum + root.data)
        else:
            if (leftSum > rightSum):
                return (leftHeight + 1, leftSum + root.data)
            else:
                return (rightHeight + 1, rightSum + root.data)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol = Solution()
    print(sol.sumOfLongRootToLeafPath(root))
