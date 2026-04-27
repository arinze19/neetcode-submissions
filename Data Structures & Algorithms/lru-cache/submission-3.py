class ListNode:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    """
    class ListNode:
        def __init__ (self, val=0, next=None):
            self.val = val
            self.next = next
    """

    def __init__(self, capacity: int):
        # initialize with a capacity: c
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0)
        self.curr = ListNode(0)

        # link dummy nodes
        self.head.next = self.curr
        self.curr.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # if key in cache, update position of pointer
            item = self.cache[key]

            item.prev.next = item.next
            item.next.prev = item.prev

            # temp
            temp = self.curr.prev 

            # update front
            item.next = self.curr
            self.curr.prev = item

            # update back
            item.prev = temp
            temp.next = item
            
            # return value
            return self.curr.prev.val
        return -1

    def put(self, key: int, value: int) -> None:
        # create new node
        item = ListNode(value, key)

        if key in self.cache:
            # remove previous node
            stale_item = self.cache[key]

            # update pointers
            stale_item.prev.next = stale_item.next
            stale_item.next.prev = stale_item.prev 

        # add node to the front of list
        temp = self.curr.prev 

        temp.next = item
        item.prev = temp

        item.next = self.curr
        self.curr.prev = item

        # update hash map
        self.cache[key] = item

        if len(self.cache) > self.capacity:
            lru_item = self.head.next
            lru_item.next.prev = self.head
            self.head.next = lru_item.next
            del self.cache[lru_item.key]

