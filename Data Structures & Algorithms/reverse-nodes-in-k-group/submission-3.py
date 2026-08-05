# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Account for empty node
        ^ = prev
        * = curr (prev.next)
        count = 0

        [dummy] -> [3] -> [2] -> [1] -> [4] -> [5] -> [6]
          ^                              *
        while True

        while curr != None and count < k:
            count += 1
            curr = curr.next

        if count == k:
            reversed = reverse(prev.next, curr)
            prev.next = reversed
            prev = curr
        else count < k:
            return dummy.next

        reverse(node1, node2):
            prev = node2
            curr = node1
            count = k

            while count: # reverse up until count
                next__ = curr.next
                curr.next = prev
                prev = curr
                curr = next__
                count -= 1

            return prev
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next

        def reverse(node1, node2):
            prev = node2
            curr = node1
            count = k

            while count:
                next__ = curr.next
                curr.next = prev 
                prev = curr 
                curr = next__
                count -= 1

            return prev 

        while True:
            count = 0

            while curr and count < k:
                count += 1
                curr = curr.next

            if count < k:
                return dummy.next

            next__ = prev.next
            prev.next = reverse(next__, curr)
            prev = next__ # reset prev
            curr = next__.next # reset curr
            count = 0 # reset count

        return None


        
