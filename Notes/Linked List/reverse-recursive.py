def reverse_recursive(head):
    if head is None or head.next is None:
        # base case: this is the new head
        return head
    new_head = reverse_recursive(head.next)
    # the node ahead points back at me
    head.next.next = head
    # I now terminate the list
    head.next = None
    return new_head