# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Loop detected
                # Reassign fast pointer to head of LL
                fast = head
                while slow != fast:  # Find starting point of loop
                    slow = slow.next
                    fast = fast.next

                return slow

        return None
