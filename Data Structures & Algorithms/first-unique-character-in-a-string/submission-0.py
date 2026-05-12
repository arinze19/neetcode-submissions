class Solution:
    def firstUniqChar(self, s: str) -> int:
        # time: O(n)
        # space: O(n)
        cache = {}

        for i in range(len(s)):
            char = s[i] # store current character

            if char not in cache:
                cache[char] = []

            cache[char].append(i)


        for char in cache:
            if len(cache[char]) == 1:
                return cache[char][0]


        return -1
            
                

            