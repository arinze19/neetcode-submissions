# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reorder the linkedlist
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow, None

        while curr:
            next__ = curr.next 
            curr.next = prev
            prev = curr
            curr = next__

        # reset curr to head and attach to prev and then backtrack
        curr = head

        while prev and prev.next:
            next__ = curr.next
            prev_next__ = prev.next
            curr.next = prev
            prev.next = next__
            curr = next__
            prev = prev_next__

