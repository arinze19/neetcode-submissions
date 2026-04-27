# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # remove all instances of val in the list 
        # create a dummy node
        
        # INPUT AND OUTPUT 
        # list can be empty
        # max value is 50 and min value is 0
        # can we return a new list?? [no] (sort list in place)

        # THOUGHT PROCESS 
        # create a dummy node
        # prev = dummy node
        # curr = head 
        # while curr 
        # if curr.val == val:
        #   temp = curr.next
        #   prev.next = temp
        #   curr.next = None
        #   curr = temp
        # else
        #   prev = curr
        #   curr = curr.next
        # return dummy.next

        # EDGE CASES
        # N/A
        dummy = ListNode()
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                temp = curr.next
                prev.next = temp
                curr.next = None
                curr = temp
            else:
                prev.next = curr
                prev = curr
                curr = curr.next

        return dummy.next
        