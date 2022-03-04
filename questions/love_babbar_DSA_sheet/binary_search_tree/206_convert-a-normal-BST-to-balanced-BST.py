from math import floor


class TreeNode:
    def __init__(self, val):
        self.right = None
        self.val = val
        self.left = None


class Solution:
    def inorderTraversal(self, root, inTrav):
        if (root):
            self.inorderTraversal(root.left, inTrav)
            inTrav.append(root.val)
            self.inorderTraversal(root.right, inTrav)

    def balancedBST(self, root):
        inTrav = []
        self.inorderTraversal(root, inTrav)
        return self.balancedBSTUtil(inTrav)

    def balancedBSTUtil(self, arr):
        if (len(arr) <= 0):
            return None

        midIndex = floor(len(arr)/2)
        root = TreeNode(arr[midIndex])
        root.left = self.balancedBSTUtil(arr[:midIndex])
        root.right = self.balancedBSTUtil(arr[midIndex+1:])
        return root


if __name__ == '__main__':

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    sol = Solution()
    balancedRoot = sol.balancedBST(root)
    inTrav = []
    sol.inorderTraversal(balancedRoot, inTrav)
    print(inTrav)
