from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def topView(self, root):
        if (root is None):
            return

        hDist = 0
        hashMap = {}
        queue = deque()
        queue.append((root, hDist))

        while (queue):
            currNode, hDist = queue.popleft()
            if (hDist not in hashMap.keys()):
                hashMap[hDist] = []
            hashMap[hDist].append(currNode.data)

            if (currNode.left):
                queue.append((currNode.left, hDist - 1))
            if (currNode.right):
                queue.append((currNode.right, hDist + 1))

        result = []
        for key in sorted(hashMap.keys()):
            result.append(hashMap[key][0])

        return result


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    sol = Solution()
    print(sol.topView(root))
