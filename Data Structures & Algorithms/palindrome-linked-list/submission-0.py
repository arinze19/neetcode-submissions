# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle of the linked list
        # reverse from the middle 
        # shift right and left at select speeds 

        # find middle of list 
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        

        # [1,2,2,1]
        #    s f
        #      s   f
        # everything after the middle should just start reversing
        fast = self.reverseList(slow)
        slow = head


        while fast:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next

        return True
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp
        
        return prev
