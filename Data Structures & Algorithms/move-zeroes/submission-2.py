class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        c = len(nums) # length of input


        for right in range(c): # starting in the range of left to end of c
            # if right is nonZero, swap
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1