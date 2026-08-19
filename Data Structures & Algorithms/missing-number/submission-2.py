class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        KEYWORDS
        1. no duplicates 

        QUESTIONS
        1. is the numb sorted?
        2. will there always be an answer? no? return 0
        3. will there only be one missing

        THOUGH PROCESS
        1. loop from 1 to n and pop from the set 
            - if set is not empty, return list(set)[0] - first item in the set
        2. binary search? 
            - 
        3. loop and keep making sure the next item is 1 greater than the previous
        
        FOLLOW UP 
        1. O(1) space and O(n) time
        '''
        cache = set()

        for i in range(len(nums)):
            cache.add(nums[i])

        for j in range(len(nums) + 1):
            if j not in cache:
                return j

        return 0
