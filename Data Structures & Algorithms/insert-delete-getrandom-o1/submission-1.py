import random

'''
KEYWORDS 
1. randomized_set -> initate class
2. insert -> 
3. remove -> 
4. getRandom -> guaranteed that at least on element exist when called 
    - each element must have the same probablity of being returned 
5. must implement function that runs in average of O(1) time 

QUESTIONS 
1. can update? does insert update or is the operation rejected outright
'''

class RandomizedSet:
    '''
    cache = { 1: 0 }
    entities = [1]
    '''

    def __init__(self):
        # cache = hold the index and the items 
        # entities = []
        self.cache = {}
        self.entities = []

    def insert(self, val: int) -> bool:
        # check the cache if avalialbe
        # if so, return False 
        # if not, add to cache with index of last; add to entities 
        if val in self.cache:
            return False 

        idx = len(self.entities)

        self.cache[val] = idx
        self.entities.append(val)
        

    def remove(self, val: int) -> bool:
        # check if cache if available 
        # if not, return False
        # if so, delete from cache
        # swap with last item on entities 
        if val not in self.cache:
            return False 

        size = len(self.entities) - 1 # 0
        idx = self.cache[val] # 0
        last_value = self.entities[-1] # 1

        # swap the index with last 
        self.entities[-1], self.entities[idx] = self.entities[idx], self.entities[-1]
        
        self.cache[self.entities[-1]] = size
        self.cache[last_value] = idx

        # update cache
        self.entities.pop()
        del self.cache[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.entities)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()