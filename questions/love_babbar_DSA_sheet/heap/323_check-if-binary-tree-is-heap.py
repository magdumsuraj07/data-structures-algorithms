# Question Link :
# https://practice.geeksforgeeks.org/problems/is-binary-tree-heap/1

class Node(object):
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def countBinaryTreeNodes(root):
    if root is None:
        return 0

    else:
        return (1 + countBinaryTreeNodes(root.left)
                  + countBinaryTreeNodes(root.right))


def isCompleteBinaryTree(root, nodeCount, index):
    if root is None:
        return True

    if index >= nodeCount:
        return False

    else:
        return isCompleteBinaryTree(root.left, nodeCount, index * 2 + 1) \
            and isCompleteBinaryTree(root.right, nodeCount, index * 2 + 2)


def checkMaxHeapProperty(root):
    if root is None:
        return True

    if (root.left and root.left.data > root.data) \
            or (root.right and root.right.data > root.data):
        return False

    return checkMaxHeapProperty(root.left) and checkMaxHeapProperty(root.right)


def isMaxHeap(root):
    nodeCount = countBinaryTreeNodes(root)
    if isCompleteBinaryTree(root, nodeCount, index=0) \
            and checkMaxHeapProperty(root):
        return True
    else:
        return False


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(2)
    root.right = Node(3)
    print(isMaxHeap(root))
