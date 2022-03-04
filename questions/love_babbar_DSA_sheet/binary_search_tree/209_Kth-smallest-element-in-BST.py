class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.visitedCount = 0
        self.kthSmall = -1

    # Return the Kth smallest element in the given BST
    def KthSmallestElement(self, root, K):
        # code here.
        self.KthSmallestElementUtil(root, K)
        return self.kthSmall

    def KthSmallestElementUtil(self, root, K):
        if (root):
            self.KthSmallestElementUtil(root.left, K)
            self.visitedCount += 1
            if (self.visitedCount == K):
                self.kthSmall = root.data
            self.KthSmallestElementUtil(root.right, K)


if __name__ == '__main__':

    root = Node(4)
    root.left = Node(2)
    root.right = Node(9)
    sol = Solution()
    print(sol.KthSmallestElement(root, 2))
