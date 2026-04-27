# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # while child is not null
        # prev = None
        # store next in a variable = current.next
        # current.next = prev
        # store current node in prev = prev = current
        # current = next
        """
        prev = None | next = 1 | current.next = None | prev = 0 | current = 1
        """
        prev_node = None
        next_node = None

        while head:
            # store the next variable 
            next_node = head.next # we are right here 
            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node


        