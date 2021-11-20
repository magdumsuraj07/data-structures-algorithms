class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, val):
    if (root is None):
        return Node(val)
    else:
        if (root.data == val):
            return root
        elif (root.data < val):
            root.right = insert(root.right, val)
        else:
            root.left = insert(root.left, val)
    return root


def delete(root, key):
    """
    Deletes the node with value equal to key from given BST
    """
    if (root is None):
        return root
    if (key < root.data):
        # Search in left subtree
        root.left = delete(root.left, key)
    elif (key > root.data):
        # Search in right subtree
        root.right = delete(root.right, key)
    else:
        # key == data of current node
        # Case 1/2 : Node to be deleted has 0/1 child
        if (root.left is None):
            temp = root.right
            root = None
            return temp
        elif (root.right is None):
            temp = root.left
            root = None
            return temp
        else:
            # Case 3 : Node to be deleted has 2 childs
            temp = findSuccesor(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
    return root


def findSuccesor(root):
    curr = root
    while (curr.left is not None):
        curr = curr.left
    return curr


def inorderPrint(root):
    if (root is None):
        return
    inorderPrint(root.left)
    print(root.data, end=" ")
    inorderPrint(root.right)
