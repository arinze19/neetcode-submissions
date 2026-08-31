class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        KEYWORDS
        1. in-place 

        QUESTIONS 
        1. length of array can be no less than one 

        THOUGHT PROCESS
        1. two pointers 
            - look for 0's and move to the front
            - look for 1's and move to the front
        2. stack? monotonic

        TIME AND SPACE 
        1. time | O(2n)
        2. space | O(1)

        [1,0,0,1,2] 
        
        - firstNonZero location
        nonZero = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                nums[nonZero], nums[right] = nums[right], nums[nonZero]
                nonZero += 1

        nonOne = nonZero

        for right in range(nonZero, len(nums)):
            if nums[right] == 1:
                nums[right], nums[nonOne] = nums[nonOne], nums[right]
                nonOne += 1
        '''
        nonZero = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                nums[nonZero], nums[right] = nums[right], nums[nonZero]
                nonZero += 1

        nonOne = nonZero

        for right in range(nonZero, len(nums)):
            if nums[right] == 1:
                nums[right], nums[nonOne] = nums[nonOne], nums[right]
                nonOne += 1
       
