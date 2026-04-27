# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # INPUT AND OUTPUT 
        # n is even | n is not 0 based
        # 0-indexed 
        # if 0 <= i <= (n / 2) - 1

        # [5,4,2,1]
        # i = 0 | 

        # input nodes are even

        # THOUGHT PROCESS 

        # EDGE CASES 
        # [3,2]
        arr = []
        curr = head
        res = float("-inf")

        while curr:
            arr.append(curr)
            curr = curr.next
        
        i = 0
        j = len(arr) - 1

        while i < j:
            res = max(res, arr[i].val + arr[j].val)
            i += 1
            j -= 1
        return res
