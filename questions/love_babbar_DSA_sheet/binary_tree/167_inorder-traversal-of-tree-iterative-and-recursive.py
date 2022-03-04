from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversalRecursive(self, root):
        if (root is None):
            return

        self.inorderTraversalRecursive(root.left)
        self.result.append(root.data)
        self.inorderTraversalRecursive(root.right)

    def inorderTraversalIterative(self, root):
        stack = deque()
        curr = root

        # Stop when stack is empty and curr is None
        while(stack or curr):
            if (curr):
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.result.append(curr.data)
                curr = curr.right


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    sol = Solution()
    sol.inorderTraversalRecursive(root)
    print("Inorder Traversal Recursive : ", sol.result)

    sol.result = []
    sol.inorderTraversalIterative(root)
    print("Inorder Traversal Iterative : ", sol.result)
