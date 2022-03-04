from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def printBoundaryView(self, root):
        if (root is None):
            return

        out = [root.data]
        self.addLeftBoundary(root, out)
        self.addLeafNodes(root, out)
        self.addRightBoundary(root, out)

        return out

    # This method adds left boundary of given tree excluding
    # root node and leaf nodes
    def addLeftBoundary(self, root, out):
        curr = root.left
        while (curr):
            if (not(curr.left is None and curr.right is None)):
                out.append(curr.data)
            if (curr.left):
                curr = curr.left
            else:
                curr = curr.right

    # This method adds right boundary of given tree in bottom
    # up direction excluding root node and leaf nodes
    def addRightBoundary(self, root, out):
        res = []
        curr = root.right
        while (curr):
            if (not (curr.left is None and curr.right is None)):
                res.append(curr.data)
            if (curr.right):
                curr = curr.right
            else:
                curr = curr.left
        out.extend(reversed(res))

    # This method adds leaf nodes of given tree
    def addLeafNodes(self, root, out):
        if (root.left is None and root.right is None):
            out.append(root.data)
        if (root.left):
            self.addLeafNodes(root.left, out)
        if(root.right):
            self.addLeafNodes(root.right, out)


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

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    # root = buildTree("12 11 12 7 1 12 14 11 N 7 3 6 4 12 7 14 14 N 2 10 8 7")
    sol = Solution()
    print(sol.printBoundaryView(root))
