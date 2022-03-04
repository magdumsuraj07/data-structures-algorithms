from math import floor


class TreeNode:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None


class Solution:
    def inorderTraversal(self, root, inTrav):
        if (root):
            self.inorderTraversal(root.left, inTrav)
            inTrav.append(root.data)
            self.inorderTraversal(root.right, inTrav)

    def mergeTwoSortedArray(self, arr1, arr2):
        merged = []
        i = j = 0
        n1 = len(arr1)
        n2 = len(arr2)
        while (i < n1 and j < n2):
            if (arr1[i] < arr2[j]):
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        while (i < n1):
            merged.append(arr1[i])
            i += 1
        while (j < n2):
            merged.append(arr2[j])
            j += 1

        return merged

    def sortedArrayToBST(self, arr):
        if (len(arr) <= 0):
            return None
        midIndex = floor(len(arr)/2)
        root = TreeNode(arr[midIndex])
        root.left = self.sortedArrayToBST(arr[:midIndex])
        root.right = self.sortedArrayToBST(arr[midIndex+1:])
        return root

    def mergeTwoBST(self, root1, root2):
        inTravA = []
        inTravB = []
        self.inorderTraversal(root1, inTravA)
        self.inorderTraversal(root2, inTravB)

        inTravMerged = self.mergeTwoSortedArray(inTravA, inTravB)
        newRoot = self.sortedArrayToBST(inTravMerged)
        return newRoot


if __name__ == '__main__':

    root1 = TreeNode(3)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)

    root2 = TreeNode(4)
    root2.left = TreeNode(1)
    root2.right = TreeNode(6)
    sol = Solution()
    mergedRoot = sol.mergeTwoBST(root1, root2)
    inTrav = []
    sol.inorderTraversal(mergedRoot, inTrav)
    print(inTrav)
