class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def countPairs(self, root1, root2, x):
        hMap = {}
        pairCount = [0]
        self.createHashmap(root2, hMap)
        self.countPairsUtil(root1, hMap, x, pairCount)
        return pairCount[0]

    def countPairsUtil(self, root, hMap, x, pairCount):
        if (root):
            self.countPairsUtil(root.left, hMap, x, pairCount)
            target = x - root.data
            if (target in hMap.keys()):
                pairCount[0] += 1
            self.countPairsUtil(root.right, hMap, x, pairCount)

    def createHashmap(self, root, hMap):
        if (root):
            self.createHashmap(root.left, hMap)
            if (root.data not in hMap.keys()):
                hMap[root.data] = 0
            else:
                hMap[root.data] += 1
            self.createHashmap(root.right, hMap)


if __name__ == '__main__':
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(7)
    root1.left.left = Node(2)
    root1.left.right = Node(4)
    root1.right.left = Node(6)
    root1.right.right = Node(8)

    root2 = Node(10)
    root2.left = Node(6)
    root2.right = Node(15)
    root2.left.left = Node(3)
    root2.left.right = Node(8)
    root2.right.left = Node(11)
    root2.right.right = Node(18)
    print(Solution().countPairs(root1, root2, x=16))
