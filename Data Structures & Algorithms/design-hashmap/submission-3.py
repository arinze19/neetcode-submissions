class Node:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.val = value
        self.next = next

class MyHashMap:
    '''
    Questions
    1. input cannot be empty for both put and remove 
    2. 

    Thought process 
    1. we can use an array as the storage and index as the key
    2. 
    '''

    def __init__(self):
        self.head = Node() # dummy node
        
    def put(self, key: int, value: int) -> None:
        # if key in cache
        # remove the item, add it back
        self.remove(key)
        
        head = self.head
        node = Node(key, value, head.next)

        head.next = node

    def get(self, key: int) -> int:
        curr = self.head.next

        while curr:
            if curr.key == key:
                return curr.val

            curr = curr.next

        return -1
        
    def remove(self, key: int) -> None:
        curr = self.head

        while curr and curr.next:
            next__ = curr.next

            if next__.key == key:
                curr.next = next__.next
                next__.next = None # reset next 

            curr = curr.next
            
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)