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
        
        cache = set(nums)
        longest = 0

        for num in nums:
            # only start counting once the current number "starts" a sequence
            if num - 1 not in cache:
                local_longest = 1
                next_num = num + 1

                # increment count while next number is in the cache
                while next_num in cache:
                    local_longest += 1
                    next_num += 1

                longest = max(local_longest, longest) # updat the longest count

        return longest
        

       