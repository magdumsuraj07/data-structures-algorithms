from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def zigZagTraversal(root):
    if (root is None):
        return []

    q = deque()
    q.append(root)
    result = []
    currLevel = 1

    while (len(q)):
        n = len(q)
        currLevelNodes = []
        for i in range(n):
            temp = q.popleft()
            currLevelNodes.append(temp.data)

            if (temp.left is not None):
                q.append(temp.left)
            if (temp.right is not None):
                q.append(temp.right)

        if (currLevel % 2 == 0):
            currLevelNodes.reverse()
        result.extend(currLevelNodes)
        currLevel += 1

    return result


if __name__ == '__main__':

    root = Node(7)
    root.left = Node(9)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(8)
    root.right.left = Node(6)
    root.left.left.left = Node(10)
    root.left.left.right = Node(9)

    print(zigZagTraversal(root))
