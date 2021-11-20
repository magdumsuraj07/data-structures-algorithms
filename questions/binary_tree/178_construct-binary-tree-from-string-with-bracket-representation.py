from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def treeFromString(self, S):
        stack = deque()
        for ch in S:
            if ch.isdigit():
                stack.append(Node(int(ch)))
            if ch == ')':
                currNode = stack.pop()
                parentNode = stack[-1]
                if (parentNode.left is None):
                    parentNode.left = currNode
                else:
                    parentNode.right = currNode
        return stack[0]


def preorderTraversal(root):
    if (root is None):
        return
    print(root.data)
    preorderTraversal(root.left)
    preorderTraversal(root.right)


if __name__ == '__main__':

    sol = Solution()
    root = sol.treeFromString("4(2(3)(1))(6(5))")
    preorderTraversal(root)
