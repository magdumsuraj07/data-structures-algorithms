# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseLL(self, head):
        prev = nxt = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle of LL
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half of LL
        slow.next = self.reverseLL(slow.next)

        # Move slow to right half
        slow = slow.next

        # Check is left half and right half are same or not
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True
