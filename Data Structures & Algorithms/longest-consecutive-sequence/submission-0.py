class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Exactly one greater than the previous

        BRUTE FORCE
        1. for each loop count how many are consecutive
        
        OPTIMIZED
        1. sort 
        2. calculate conditions 

        hash map initiated to 0
        loop through array again and increment
        { 2: 0, 20: 0, 4: 0 }
        '''
        cache = { i: i for i in nums }
        visited = set()
        res = 0

        for num in nums:
            curr = num
            count = 0

            if num in visited:
                continue 

            while curr in cache:
                count += 1
                curr += 1
                visited.add(curr)

            res = max(count, res)

        return res