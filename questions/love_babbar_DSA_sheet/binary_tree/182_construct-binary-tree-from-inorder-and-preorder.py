class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.idx = 0

    def buildTree(self, inorder, preorder):
        return self.buildTreeUtil(inorder, preorder, 0, len(preorder)-1)

    def buildTreeUtil(self, inorder, preorder, start, end):
        if (start > end):
            return None

        currData = preorder[self.idx]
        self.idx += 1
        currNode = Node(currData)
        if (start == end):
            return currNode

        pos = inorder.index(currData, start, end+1)
        currNode.left = self.buildTreeUtil(inorder, preorder, start, pos-1)
        currNode.right = self.buildTreeUtil(inorder, preorder, pos+1, end)

        return currNode


def preorderPrint(root):
    if (root is None):
        return
    print(root.data)
    preorderPrint(root.left)
    preorderPrint(root.right)


if __name__ == '__main__':
    inorder = [3, 1, 4, 0, 5, 2]
    preorder = [0, 1, 3, 4, 2, 5]
    sol = Solution()
    root = sol.buildTree(inorder, preorder)
    preorderPrint(root)
