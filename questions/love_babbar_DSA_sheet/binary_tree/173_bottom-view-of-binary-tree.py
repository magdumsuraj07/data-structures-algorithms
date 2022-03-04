from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def bottomView(self, root):
        if (root is None):
            return

        hDist = 0
        hashMap = {}
        queue = deque()
        queue.append((root, hDist))

        while(queue):
            currNode, hDist = queue.popleft()

            if (hDist not in hashMap.keys()):
                hashMap[hDist] = []
            hashMap[hDist].append(currNode.data)

            if (currNode.left):
                queue.append((currNode.left, hDist - 1))

            if(currNode.right):
                queue.append((currNode.right, hDist + 1))

        result = []
        for key in sorted(hashMap.keys()):
            result.append(hashMap[key][-1])

        return result


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    sol = Solution()
    print(sol.bottomView(root))
