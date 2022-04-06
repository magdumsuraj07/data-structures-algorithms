# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseLinkedList(self, head):
        curr = head
        prev = nxt = None

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Return head and tail of reversed LL
        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        h1 = t1 = head
        count = 1

        while t1.next and count < k:
            t1 = t1.next
            count += 1

        if count == k:
            h2 = t1.next
            t1.next = None
            h1, t1 = self.reverseLinkedList(h1)
            t1.next = self.reverseKGroup(h2, k)

        return h1
