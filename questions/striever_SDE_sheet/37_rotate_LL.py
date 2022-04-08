# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        # Count no. of nodes in LL
        nodesCount = 1
        temp = head
        while temp.next:
            temp = temp.next
            nodesCount += 1

        # Make tail.next = head
        temp.next = head

        # If k > no. of nodes
        k = k % nodesCount

        k = nodesCount - k

        while k > 0:
            temp = temp.next
            k -= 1

        head = temp.next
        temp.next = None

        return head
