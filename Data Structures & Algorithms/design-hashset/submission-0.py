class MyHashSet:

    def __init__(self):
        # adds a key to the hash-set
        # verifies is a key exists in the hash set
        # removes a key from the hash set. else do nothing

        # INPUT AND OUTPUT
        # - key can be 0
        # - key cannot be negative 
        # - does this mean we cannot use hash maps??? [we cannot use hash maps]

        # THOUGHT PROCESS
        # - create an array to add items 
        # - to remove items we can just remove from the array
        # - to verify if contains we can simply scan items
        self.items = []

    def add(self, key: int) -> None:
        # call contains | if contains, return
        if self.contains(key): 
            return 

        self.items.append(key) 
        
    def remove(self, key: int) -> None:
        # verify if can remove 
        if not self.contains(key):
            return
        
        self.items.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.items
        

    # RUNTIME
    # space O(n)
    # time 
    #   - add O(n) 
    #   - remove O(n)
    #   - contains O(n)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)