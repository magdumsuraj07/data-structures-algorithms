class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.maxSum = 0

    def largestSubtreeSum(self, root):
        self.largestSubtreeSumUtil(root)
        return self.maxSum

    def largestSubtreeSumUtil(self, root):

        if (root is None):
            return 0

        leftSum = self.largestSubtreeSumUtil(root.left)
        rightSum = self.largestSubtreeSumUtil(root.right)
        currSum = leftSum + rightSum + root.data

        if (self.maxSum < currSum):
            self.maxSum = currSum

        return currSum


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(-2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(-6)
    root.right.right = Node(2)

    sol = Solution()
    print(sol.largestSubtreeSum(root))
