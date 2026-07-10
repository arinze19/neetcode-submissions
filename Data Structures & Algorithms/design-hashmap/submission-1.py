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
        self.cache = [-1] * 1_000_001
        
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        

    def get(self, key: int) -> int:
        return self.cache[key]
        

    def remove(self, key: int) -> None:
        self.cache[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)