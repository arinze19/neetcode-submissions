class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cache = set()

        for i in range(len(nums)):
            if nums[i] in cache:
                return nums[i]
            else:
                cache.add(nums[i])