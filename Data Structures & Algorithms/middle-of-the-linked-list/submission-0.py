# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # INPUT AND OUTPUT 
        # length of the list is (1, 100)
        # return the middle node as is 

        # THOUGHT PROCESS 
        # traverse with a fast and slow pointer until fast pointer is None (or its next is none)

        # EDGE CASES
        
        fast = head 
        slow = head 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow