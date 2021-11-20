class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def findPath(root, key, path):
    if (root is None):
        return False

    path.append(root.data)
    if (root.data == key):
        return True
    if (findPath(root.left, key, path) or findPath(root.right, key, path)):
        return True
    path.pop()
    return False


def kthAncestor(root, node, K):
    path = []
    isPathPresent = findPath(root, node, path)
    if (not isPathPresent):
        return -1
    if (K > len(path)-1):
        return -1
    return path[-(K+1)]


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(kthAncestor(root, 5, 2))
