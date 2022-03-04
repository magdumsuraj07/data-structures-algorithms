from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def dupSubtree(self, root):
        queue = deque()
        queue.append(root)
        hMap = {}
        while (queue):
            curr = queue.popleft()
            out = []
            #  For leaf nodes; don't need to check
            if not(curr.left is None and curr.right is None):
                self.inorderTraversal(curr, out)

                if (curr.data not in hMap.keys()):
                    hMap[curr.data] = [out]
                else:
                    for trav in hMap[curr.data]:
                        if (trav == out):
                            return 1
                    hMap[curr.data].append(out)

                if (curr.left):
                    queue.append(curr.left)
                if (curr.right):
                    queue.append(curr.right)

        return 0

    def inorderTraversal(self, root, out):
        if (root is None):
            return
        self.inorderTraversal(root.left, out)
        out.append(root.data)
        self.inorderTraversal(root.right, out)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(2)
    root.right.right.left = Node(4)
    root.right.right.right = Node(5)

    sol = Solution()
    print(sol.dupSubtree(root))
