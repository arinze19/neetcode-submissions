# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # INPUT AND OUTPUT 
        pt1 = headA
        pt2 = headB

        while pt1 != pt2:
            pt1 = pt1.next if pt1 else headB
            pt2 = pt2.next if pt2 else headA

        return pt1
        # THOUGH PROCESS 
        # maybe we can go in a cycle?
        # fast and slow pointer style; except this is just a normal pointer moving at a normal pace

        # EDGE CASES 
