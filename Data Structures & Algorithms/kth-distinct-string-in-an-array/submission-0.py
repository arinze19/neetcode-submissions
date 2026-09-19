from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        blocked = set()
        cache = defaultdict(int)
        count = 0

        # get all distint elements 
        for char in arr:
            if char not in cache and char not in blocked:
                cache[char] += 1
            elif char in cache and char not in blocked:
                blocked.add(char)
                del cache[char]

        # get the kth value
        res = list(cache.keys())

        return "" if k > len(res) else res[k - 1]        