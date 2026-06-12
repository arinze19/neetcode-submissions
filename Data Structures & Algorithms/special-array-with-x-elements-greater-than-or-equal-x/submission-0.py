class Solution:
    def specialArray(self, nums: List[int]) -> int:
        '''
        Questions 
        1. can the input nums be sorted 
        2. 

        Thought process 
        1. sort the array
        2. get the mid point (mid)
        '''
        for i in range(1, len(nums) + 1):
            count = 0
            for j in range(len(nums)):
                if nums[j] >= i:
                    count += 1

            if count == i:
                return i

        return -1