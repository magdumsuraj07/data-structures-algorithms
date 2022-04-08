class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def mergeTwoSortedLL(l1, l2):
    dummy = Node(None)
    temp = dummy
    while l1 and l2:
        if l1.data < l2.data:
            temp.bottom = l1
            l1 = l1.bottom
        else:
            temp.bottom = l2
            l2 = l2.bottom
        temp = temp.bottom

    # Copy remaining elements of list 1
    while l1:
        temp.bottom = l1
        temp = temp.bottom
        l1 = l1.bottom

    # Copy remaining elements of list 2
    while l2:
        temp.bottom = l2
        temp = temp.bottom
        l2 = l2.bottom

    return dummy.bottom


def flatten(root):
    if root.next is None:
        return root

    l2 = flatten(root.next)

    return mergeTwoSortedLL(root, l2)
