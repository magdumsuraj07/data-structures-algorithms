from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def diagonalTraversal(root):
    if (root is None):
        return

    queue = deque()
    currNode = root
    result = []
    while (currNode):
        result.append(currNode.data)

        if (currNode.left):
            queue.append(currNode.left)
        if (currNode.right):
            currNode = currNode.right
        else:
            if (len(queue) > 0):
                currNode = queue.popleft()
            else:
                currNode = None
    return result


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


if __name__ == '__main__':

    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right.left = Node(13)
    # root = buildTree("12 11 12 7 1 12 14 11 N 7 3 6 4 12 7 14 14 N 2 10 8 7")
    print(diagonalTraversal(root))
