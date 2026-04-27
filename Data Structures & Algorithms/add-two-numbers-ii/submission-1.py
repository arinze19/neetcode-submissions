import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # I gues the trick here is that we have to start from the end? 
        # reverse both linked list
        # solve for node addition
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        carry = 0
        curr = None

        while l1 or l2 or carry:
            # add two numbers 
            first = getattr(l1, "val", 0)
            second = getattr(l2, "val", 0)
            total = first + second + carry

            # if total extends more than single digit
            count = total % 10
            carry = total // 10

            curr = ListNode(count, curr)

            # move pointers 
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return curr

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp

        return prev