class BinaryTreeNode:
    '''
    This class represents a node in Binary Search Tree
    '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        '''
        Constructor for BinarySearchTree class.
        '''
        self.root = None
        self.numNodes = 0

    def __printTreeHelper(self, root):
        '''
        Helper method for printTree() method.
        '''
        if (root is None):
            return
        if (root.left and root.right):
            print("{}:L:{},R:{}".format(root.data, root.left.data,
                  root.right.data))
            self.__printTreeHelper(root.left)
            self.__printTreeHelper(root.right)
        elif (root.left):
            print("{}:L:{},".format(root.data, root.left.data))
            self.__printTreeHelper(root.left)
        elif (root.right):
            print("{}:R:{}".format(root.data, root.right.data))
            self.__printTreeHelper(root.right)
        else:
            print(str(root.data) + ":")

    def printTree(self):
        '''
        Print binary tree.
        '''
        self.__printTreeHelper(self.root)

    def __searchHelper(self, root, data):
        '''
        Helper method for search() method.
        '''
        if (root is None):
            return False
        if (root.data == data):
            return True
        if (data < root.data):
            return self.__searchHelper(root.left, data)
        else:
            return self.__searchHelper(root.right, data)

    def search(self, data):
        '''
        Serach node in binary search tree.
        '''
        return self.__searchHelper(self.root, data)

    def __insertHelper(self, root, data):
        '''
        Helper method for insert() method.
        '''
        if (root is None):
            node = BinaryTreeNode(data)
            return node
        if (data <= root.data):
            root.left = self.__insertHelper(root.left, data)
        else:
            root.right = self.__insertHelper(root.right, data)
        return root

    def insert(self, data):
        '''
        Insert a node into binary search tree.
        '''
        self.root = self.__insertHelper(self.root, data)
        self.numNodes += 1

    def __deleteHelper(self, root, data):
        '''
        Helper method for delete() method.
        '''
        if (root is None):
            return False, None
        if (data < root.data):
            deleted, root.left = self.__deleteHelper(root.left, data)
            return deleted, root
        if (data > root.data):
            deleted, root.right = self.__deleteHelper(root.right, data)
            return deleted, root

        # root is leaf
        if (root.left is None and root.right is None):
            return True, None

        # root has one child
        if (root.left is None):
            return True, root.right
        if (root.right is None):
            return True, root.left

        # root has two children
        minRight = root.right
        while (minRight.left):
            minRight = minRight.left
        root.data = minRight.data
        deleted, root.right = self.__deleteHelper(root.right, root.data)
        return deleted, root

    def delete(self, data):
        '''
        Delete a node in binary search tree.
        '''
        deleted, newRoot = self.__deleteHelper(self.root, data)
        if (deleted):
            self.numNodes -= 1
        self.root = newRoot
        return deleted

    def count(self):
        '''
        Returns a count of nodes currently present in BST
        '''
        return self.numNodes


b = BinarySearchTree()
b.insert(5)
b.insert(8)
b.insert(2)
b.insert(10)
print(b.count())
print(b.search(100))
print(b.search(8))
print(b.delete(2))
print(b.printTree())
