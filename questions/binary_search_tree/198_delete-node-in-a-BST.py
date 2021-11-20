class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMinimum(self, root):
        curr = root
        while (curr.left is not None):
            curr = curr.left
        return curr

    def deleteNode(self, root, key):
        if (root is None):
            return root

        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
        elif (key < root.val):
            root.left = self.deleteNode(root.left, key)
        else:
            if (root.left is None):
                temp = root.right
                root = None
                return temp
            elif (root.right is None):
                temp = root.left
                root = None
                return temp
            else:
                temp = self.findMinimum(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root
