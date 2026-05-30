import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        start = 0
        end = len(nums) - 1

        while start <= end:
            index = self.partition(nums, start, end)

            if target == index:
                return nums[index]
            if target < index:
                end = index - 1
            else:
                start = index + 1

        return 0
        

    def partition(self, nums, start, end):
        j = start - 1 # tracks where the pivot goes after partitioning

        for i in range(start, end):
            if nums[i] <= nums[end]:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]

        j += 1
        nums[j], nums[end] = nums[end], nums[j]

        return j
