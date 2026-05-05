class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        left = 0
        length = len(nums)

        while left < length:
            if nums[left]:
                right = left
                while right < length and nums[right]:
                    right += 1

                res = max(res, right - left)
                left = right
            else:
                left += 1

        return res
