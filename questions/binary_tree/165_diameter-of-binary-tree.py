class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Height:
    def __init__(self):
        self.h = 0


def diameter(root, height):
    if (root is None):
        height.h = 0
        return 0

    lHeight = Height()
    rHeight = Height()

    lDiameter = diameter(root.left, lHeight)
    rDiameter = diameter(root.right, rHeight)

    height.h = max(lHeight.h, rHeight.h) + 1
    currDiameter = lHeight.h + rHeight.h + 1

    return max(lDiameter, rDiameter, currDiameter)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)

    print(diameter(root, Height()))
