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
        prev = ""

        if key not in self.cache:
            return ""

        for (value, time) in self.cache[key]:
            if time <= timestamp:
                prev = value

        return prev
        
