from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversalRecursive(self, root):
        if (root is None):
            return

        self.result.append(root.data)
        self.preorderTraversalRecursive(root.left)
        self.preorderTraversalRecursive(root.right)

    def preorderTraversalIterative(self, root):
        # If tree is empty then return
        if (root is None):
            return

        stack = deque()
        stack.append(root)
        # Stop when stack is empty
        while (stack):
            curr = stack.pop()
            self.result.append(curr.data)

            if (curr.right):
                stack.append(curr.right)

            if (curr.left):
                stack.append(curr.left)


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
    sol.preorderTraversalRecursive(root)
    print("Preorder Traversal Recursive : ", sol.result)

    sol.result = []
    sol.preorderTraversalIterative(root)
    print("Preorder Traversal Iterative : ", sol.result)
