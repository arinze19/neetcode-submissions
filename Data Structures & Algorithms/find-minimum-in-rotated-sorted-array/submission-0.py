class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        if nums[mid] > nums[right]:
            - close up left
        else:
            - close up right
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        
        return nums[left]