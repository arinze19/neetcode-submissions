# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1. positions are tagged as indexes 
        2. must reorder the nodes themselves not change value

        INPUT AND OUTPUT
        1. there is at least one node

        THOUGHT PROCESS
        1. loop through list and add items to an array
        2. determine the mid-point (floor or ceil) 
        2. loop through items again and for each head[i] link its next to array[]
        """
        curr = head
        arr = []

        while curr:
            arr.append(curr)
            curr = curr.next

        i = 0
        j = len(arr) - 1

        # [1,2,3,4]
        """
        i = 0; j = 3
        arr[i].next = arr[j]
        i += 1
        if i < j - 1:
            arr[j].next = arr[i]
            j -= 1
        i = 1; j = 2
        arr[i].next = arr[j]
        i += 1
        if i < j - 1:
            arr[j].next = arr[i]
            j -= 1
        
        arr[j].next = None
        """
        i = 0
        j = len(arr) - 1

        while i < j:
            arr[i].next = arr[j]
            i += 1
            if i < j:
                arr[j].next = arr[i]
                j -= 1
            
        arr[j].next = None      