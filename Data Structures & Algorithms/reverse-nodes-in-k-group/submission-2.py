# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # temp = curr (hold a temporary reference to next node)
        # how to reverse from head until kth node
        # while curr and count > 0
        #   next__ = curr.next
        #   curr.next = prev
        #   prev = curr
        #   curr = next__
        #   count -= 1
        # head = prev
        # head.next = temp
        # EDGE CASES 
        # 
        # reverse linked list from head 
        # attach head to 
        curr = head 
        count = 0

        while curr and count < k:
            curr = curr.next 
            count += 1

        if count == k:
            temp = self.reverseKGroup(curr, k)
            curr = head
            prev = None
            while curr and count > 0:
                next__ = curr.next
                curr.next = prev 
                prev = curr
                curr = next__
                count -= 1

            head.next = temp
            head = prev

        return head
            


       
        