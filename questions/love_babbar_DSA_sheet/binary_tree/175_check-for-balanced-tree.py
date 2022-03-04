from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


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


class Height():
    def __init__(self):
        self.h = 0


def isBalanced(root, height):
    if (root is None):
        return True

    lh, rh = Height(), Height()

    if (isBalanced(root.left, lh) is False):
        return False

    if (isBalanced(root.right, rh) is False):
        return False

    height.h = max(lh.h, rh.h) + 1

    if (abs(lh.h - rh.h) <= 1):
        return True
    else:
        return False


if __name__ == '__main__':
    # s = input()
    # root = buildTree(s)
    height = Height()
    root = Node(10)
    root.left = Node(20)
    # root.right = Node(39)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)

    print(isBalanced(root, height))
