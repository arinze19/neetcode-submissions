class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Keywords
        1. positive integers nums
        2. minimal *length* of a subarray whose sum is greater than or equal to target

        Questions 
        1. 

        Thought Process
        1. Prefix sum?
            - should get familiar with what to store
        2. sliding window

        TIME AND SPACE 
        1. time | O(n)
        2. space | O(1)
        # [0,1,3,6,19,15,20]
        '''
        res = float("inf")
        prefix_sum = 0
        left = right = 0

        while right < len(nums):
            prefix_sum += nums[right] # we need to move this
            while left <=right and prefix_sum >= target:
                res = min(res, right - left + 1)
                prefix_sum -= nums[left]
                left += 1

            right += 1

        return 0 if res == float("inf") else res
            