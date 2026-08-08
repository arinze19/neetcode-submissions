# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        Keywords
        1. left <= right
        2. nodes are one indexed
        
        Questions 
        1. can we have duplicate nodes? Yes
        2. are left and right guaranteed to be in the linked list? Yes 
        3. Linked List can be empty? No
        4. start and end == same node

        Thought Process
        0. create a dummy/sentinel node
        1. look for the left node
            - while keeping track of previous node (start at dummy node)
            - prev = dummy
            - while curr and curr.val != left:
                prev = curr
                curr = curr.next
        2. look for the right node (starting from the left node)
            - while curr and curr.val != right:
                curr = curr.next
        3. swap until curr == right node?   
            reverse(node1, node2):
                # store the node1 in a variable - we are going to attach this to the end 
                prev = None
                curr = node1

                while curr != node2.next:
                    next__ = curr.next
                    curr.next = prev 
                    prev = curr
                    curr = next__

                node1.next = curr

        4. prev.next = reverse(node1, node2)
        5. return dummy.next
        '''
        def reverse(node1, node2):
            prev = None
            curr = node1
            tail = node2.next

            while curr != tail:
                next__ = curr.next
                curr.next = prev 
                prev = curr
                curr = next__

            node1.next = curr

            return prev 

        # create dummy 
        dummy = ListNode(0, head)
        leftNode = dummy.next
        rightNode = dummy.next
        prev = dummy
        count = 1

        # find left
        while leftNode and count != left:
            prev = leftNode
            leftNode = leftNode.next
            count += 1

        rightNode = leftNode # update right node 

        # find right
        while rightNode and count != right:
            rightNode = rightNode.next
            count += 1

        prev.next = reverse(leftNode, rightNode)

        return dummy.next



        