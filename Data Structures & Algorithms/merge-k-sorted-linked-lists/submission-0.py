# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Assuming the fact that we are returning a new array 
        arr = []
        res = ListNode()

        for i in range(len(lists)):
            curr = lists[i]

            while curr:
                arr.append(curr.val)
                curr = curr.next

        # sort 
        arr.sort()

        dummy = ListNode()
        prev = None

        for i in range(len(arr) - 1, -1, -1):
            item = ListNode(arr[i], prev)

            # update prev
            prev = item

            # update dummy
            dummy.next = item

        return dummy.next