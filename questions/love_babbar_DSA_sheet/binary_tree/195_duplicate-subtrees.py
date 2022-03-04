from collections import deque, OrderedDict


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root, out):
        if (root):
            out.append(root.data)
            self.preorderTraversal(root.left, out)
            self.preorderTraversal(root.right, out)

    def isExistsInResult(self, inTrav):
        for (node, trav) in self.result:
            if (inTrav == trav):
                return True
        return False

    def printAllDups(self, root):
        stack = deque()
        curr = root
        hMap = OrderedDict()
        # Stop when stack is empty and curr is None
        while(stack or curr):
            if (curr):
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                out = []
                self.preorderTraversal(curr, out)
                if (curr.data not in hMap.keys()):
                    hMap[curr.data] = [out]
                else:
                    if (out in hMap[curr.data]
                       and not self.isExistsInResult(out)):
                        self.result.append((curr, out))
                    else:
                        hMap[curr.data].append(out)

                curr = curr.right
        returnVal = []
        for (node, trav) in self.result:
            returnVal.append(node)
        return returnVal

    def _printAllDups(self, root):
        # Return if tree is empty
        if (root is None):
            return

        stack = deque()
        outStack = deque()
        hMap = {}
        stack.append(root)

        while (stack):
            curr = stack.pop()
            outStack.append(curr)

            if (curr.left):
                stack.append(curr.left)

            if (curr.right):
                stack.append(curr.right)

        while (outStack):
            curr = outStack.pop()
            out = []
            self.preorderTraversal(curr, out)
            if (curr.data not in hMap.keys()):
                hMap[curr.data] = [out]
            else:
                if (out in hMap[curr.data] and not self.isExistsInResult(out)):
                    self.result.append((curr, out))
                else:
                    hMap[curr.data].append(out)
        returnVal = []
        for (node, trav) in self.result:
            returnVal.append(node)
        return returnVal


if __name__ == '__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.right.left = Node(2)
    # root.right.right = Node(4)
    # root.right.left.left = Node(4)
    root = Node(2)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.left = Node(3)

    sol = Solution()
    result = sol._printAllDups(root)
    for res in result:
        out = []
        sol.preorderTraversal(res, out)
        print(out)
