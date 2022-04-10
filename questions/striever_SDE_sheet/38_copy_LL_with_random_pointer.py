# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # Create new LL nodes
        itr = head
        while itr:
            front = itr.next
            copy = Node(itr.val)
            itr.next = copy
            copy.next = front
            itr = front

        # Arrange random pointers
        itr = head
        while itr:
            if itr.random is not None:
                itr.next.random = itr.random.next
            itr = itr.next.next

        # Arrange next pointers
        dummy = Node(0)
        copy = dummy
        itr = head
        while itr:
            front = itr.next.next
            copy.next = itr.next
            itr = front
            copy = copy.next
            itr = itr.next

        return dummy.next
