class TimeMap:
    """
    storing values of the same key at specified stamps
    retrieving keys value at specified timestamp

    thought process:
    store this in an array?
        - problem with this is that we would need 
            to know how big the array gets 
        - reverse-index hash-map?


    """

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not already in cache, add it 
        if key not in self.cache:
            self.cache[key] = []
        
        self.cache[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""

        return self.binary_search(self.cache[key], timestamp)

    def binary_search(self, arr, target):
        # split 
        # find the part of the array where the item could be 
        # search that part
        l, r = 0, len(arr) - 1
        temp = ""

        while l <= r:
            mid = (l + r) // 2

            value, time = arr[mid]

            if time <= target:
                temp = value
                l = mid + 1
            else:
                r = mid - 1

        return temp



        
