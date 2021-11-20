class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def findDist(self, root, a, b):
        lca = self.findLCA(root, a, b)
        dist1 = self.findNode(lca, a, 0)
        dist2 = self.findNode(lca, b, 0)
        return dist1 + dist2

    def findNode(self, root, key, dist):
        if (root is None):
            return -1
        if (root.data == key):
            return dist

        left = self.findNode(root.left, key, dist+1)
        if (left != -1):
            return left
        return self.findNode(root.right, key, dist+1)

    def findLCA(self, root, a, b):
        if (root is None):
            return None

        if (root.data == a or root.data == b):
            return root

        left = self.findLCA(root.left, a, b)
        right = self.findLCA(root.right, a, b)

        if (left and right):
            return root
        elif (left):
            return left
        elif (right):
            return right


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.left.right = Node(6)
    a = 6
    b = 3
    sol = Solution()
    print(sol.findDist(root, a, b))
