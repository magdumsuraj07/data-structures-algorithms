from collections import deque


def buildTree(s):

    if (len(s) == 0 or s[0] == 'N'):
        return None

    ip = list(map(str, s.split()))

    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size += 1

    i = 1
    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size -= 1
        currVal = ip[i]

        if (currVal != "N"):
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size += 1

        i += 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        if (currVal != "N"):
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size += 1
        i += 1
    return root


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def reverseLevelOrder(self, root):
        queue = deque()
        stack = deque()

        queue.append(root)

        while(len(queue) > 0):
            temp = queue.popleft()
            stack.append(temp.data)

            if (temp.right is not None):
                queue.append(temp.right)
            if (temp.left is not None):
                queue.append(temp.left)

        res = []
        while (len(stack) > 0):
            res.append(stack.pop())

        return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        res = Solution().reverseLevelOrder(root)
        for i in res:
            print(i, end=' ')
        print()
