# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        result = ""
        carry = 0
        reverse each linked list

        reverse the linked list (both)
        account for our carry effeciently
        return the result as an int
        """
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = getattr(l1, "val", 0)
            v2 = getattr(l2, "val", 0)

            total = v1 + v2 + carry

            carry = total // 10
            val = total % 10

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        
        return dummy.next