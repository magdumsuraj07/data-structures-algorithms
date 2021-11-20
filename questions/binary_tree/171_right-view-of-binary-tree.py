from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def rightView(root):
    if (root is None):
        return []

    queue = deque()
    queue.append(root)
    result = []

    while (len(queue)):
        n = len(queue)

        for i in range(n):
            temp = queue.popleft()
            if (i == n-1):
                result.append(temp.data)

            if (temp.left is not None):
                queue.append(temp.left)

            if (temp.right is not None):
                queue.append(temp.right)

    return result


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.right = Node(8)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(rightView(root))
