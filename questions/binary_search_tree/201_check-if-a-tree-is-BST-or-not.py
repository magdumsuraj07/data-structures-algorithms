class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    # Approach 1 - Using inorder traversal
    def inorderTraversal(self, root, trav):
        if (root):
            self.inorderTraversal(root.left, trav)
            trav.append(root.data)
            self.inorderTraversal(root.right, trav)

    def isBST_1(self, root):
        inTrav = []
        self.inorderTraversal(root, inTrav)
        for i in range(len(inTrav)-2):
            if (inTrav[i] >= inTrav[i+1]):
                return 0
        return 1

    # Approach 2 : Using recursion
    def isBST_2(self, root):
        return self.validBST(root, float('-inf'), float('inf'))

    def validBST(self, root, minLimit, maxLimit):
        if (root is None):
            return True
        if (root.data <= minLimit or root.data >= maxLimit):
            return False
        return (self.validBST(root.left, minLimit, root.data)
                and self.validBST(root.right, root.data, maxLimit))


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    sol = Solution()
    print(sol.isBST_2(root))
