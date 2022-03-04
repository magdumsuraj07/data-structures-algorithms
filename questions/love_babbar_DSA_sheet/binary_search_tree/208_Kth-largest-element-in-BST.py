class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Count:
    def __init__(self):
        self.c = 0
        self.value = None


class Solution:
    def kthLargest(self, root, k):
        count = Count()
        self.kthLargestUtil(root, k, count)
        return count.value

    def kthLargestUtil(self, root, k, count):
        if (root):
            self.kthLargestUtil(root.right, k, count)
            count.c += 1
            if (count.c == k):
                count.value = root.data
            self.kthLargestUtil(root.left, k, count)


if __name__ == '__main__':

    root = Node(4)
    root.left = Node(2)
    root.right = Node(9)
    sol = Solution()
    print(sol.kthLargest(root, 2))
