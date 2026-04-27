# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        1. Are the number unique? 
            - Yes 
        2. Two pointer approach
        3. How do we terminate? when left reaches the end? 
        move front at twice the rate you move the last one 
        terminate when pt1 points to null
        """
        if not head or not head.next:
            return False
        
        pt1 = head 
        pt2 = head.next 

        while pt1 and pt2:
            if pt1 == pt2:
                return True
            else:
                pt1 = pt1.next
                if pt2.next:
                    pt2 = pt2.next.next
                else:
                    pt2 = pt2.next

        return False

        
        