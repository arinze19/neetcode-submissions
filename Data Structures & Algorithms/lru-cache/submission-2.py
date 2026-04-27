class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def get(self, key: int) -> int:
        # if key exist return corresponding value of key 
        # otherwise return -1 
        if key in self.cache:
            # delete the key and update it 
            item = self.cache[key]

            del self.cache[key]

            self.cache[key] = item

            return self.cache[key]
        
        return -1


    def put(self, key: int, value: int) -> None:
        # update the value of key value
        # if key does not exist, create new one 
        # if addition causes overflow, delete lru resource in the cache
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            for cache_key in self.cache:
                del self.cache[cache_key]
                break

        # NOTE: 
        # A key is considered used if `get` and `put` is called on it


        # INPUT AND OUTPUT
        # 1. key and value can be 0
        # 2. capacity is greater than or equal to 1

        # THOUGHT PROCESS
        # { 1: <Ox1234>, } | key: memory address mapping | this is sorted depending on how I add the items
        # add: if item not in cache, add to cache
        # update: if item in cache, update ListNode val
        #   - delete item and add to cache again (this way we keep updated order)
        # overflow: if item exceeds capacity, delete first item in mapping | also update its next by pointing it to null


        # IMPROVEMENTS
        # delete LRU node entirely to manage memory better


        # DRY RUN
        #  { 1: 10 }
        #  10
        #  { 1: 10, 2: 20, 3: 30 } | { 2: 20, 3: 30 }
