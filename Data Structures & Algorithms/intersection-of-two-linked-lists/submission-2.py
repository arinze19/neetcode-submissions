# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # INPUT AND OUTPUT 
        # return node where two lists intersect
        # if no intersection, return null
        # do not modify the linked list

        # THOUGH PROCESS 
        # we can traverse through both linked lists and put the memory address of each node 
        # into a Hash Set

        # EDGE CASES 
        # Can there be a loop within a list?
        #   1->2->3->1 | In this scenario, there is no loop between both lists but there is a loop between an individual item
        #   if this case appears we want to exit from the program and return False
        # we can have two hash sets, one to keep track of nodes in listA and one for listB

        l1 = headA
        l2 = headB
        cacheA = set()
        cacheB = set()

        while l1 or l2:
            if l1 == l2:
                return l1
                
            # validate if we have a cycle between a list 
            if l1 in cacheA or l2 in cacheB:
                return None
            
            # validate if there is an intersection 
            if l1 and l1 in cacheB:
                return l1 

            if l2 and l2 in cacheA:
                return l2

            # add to cache
            if l1:
                cacheA.add(l1)

            if l2:
                cacheB.add(l2)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return None
        """
        l1 = 1
        l2 = 3

        l1 = 9
        l2 = 6 
        """