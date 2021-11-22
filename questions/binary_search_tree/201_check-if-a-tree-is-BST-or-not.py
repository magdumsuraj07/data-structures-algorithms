class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root, trav):
        if (root):
            self.inorderTraversal(root.left, trav)
            trav.append(root.data)
            self.inorderTraversal(root.right, trav)

    def isBST(self, root):
        inTrav = []
        self.inorderTraversal(root, inTrav)
        for i in range(len(inTrav)-2):
            if (inTrav[i] >= inTrav[i+1]):
                return 0
        return 1


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    sol = Solution()
    print(sol.isBST(root))
