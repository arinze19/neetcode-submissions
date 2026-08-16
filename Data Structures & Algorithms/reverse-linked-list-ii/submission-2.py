# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head 

        dummy = ListNode(0, head)
        prev_m = dummy 

        for _ in range(left - 1):
            prev_m = prev_m.next

        end_segment = prev_m.next # this holds reference to the start of left
        prev = None
        curr = end_segment

        for _ in range(right - left + 1):
            next__ = curr.next
            curr.next = prev 
            prev = curr 
            curr = next__

        prev_m.next = prev
        end_segment.next = curr 

        return dummy.next

        