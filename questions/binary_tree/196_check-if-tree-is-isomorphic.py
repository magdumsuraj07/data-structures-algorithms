class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def isIsomorphic(self, root1, root2):
        # Return true if both the nodes are None
        if (root1 is None and root2 is None):
            return True

        # Return false if either one of two nodes is None
        if (root1 is None or root2 is None):
            return False

        # Compare the data for current nodes
        if (root1.data != root2.data):
            return False

        # Check recursively if left and right subtrees are isomorphic
        return ((self.isIsomorphic(root1.left, root2.left)
                and self.isIsomorphic(root1.right, root2.right))

                or (self.isIsomorphic(root1.left, root2.right)
                and self.isIsomorphic(root1.right, root2.left)))


if __name__ == '__main__':

    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)

    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)
    root2.left.left = Node(4)

    sol = Solution()
    print(sol.isIsomorphic(root1, root2))
