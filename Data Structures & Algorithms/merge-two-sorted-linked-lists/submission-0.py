# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. create a dummy node
        1.0 create a curr variable and point to dummy node
        1.1 pt1 = list1
        1.2 pt2 = list2
        1.3 while pt1 and pt2:
        2.  if pt1.val < pt2.val:
                curr.next = ListNode(pt1.val)
                pt1 = pt1.next
            else:
                curr.next = ListNode(pt2.val)
                pt2 = pt2.next
        3. if pt1:
                curr.next = pt1
            elif pt2:
                curr.next = pt2
        """

        head = ListNode(0)
        curr = head
        pt1 = list1
        pt2 = list2

        while pt1 and pt2:
            if pt1.val < pt2.val:
                curr.next = ListNode(pt1.val)
                pt1 = pt1.next
            else:
                curr.next = ListNode(pt2.val)
                pt2 = pt2.next
            
            curr = curr.next

        if pt1:
            curr.next = pt1
        elif pt2:
            curr.next = pt2

        return head.next
