class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minSum, maxSum = 1, 1 

        for num in nums:
            temp = num * maxSum
            maxSum = max(num, temp, num * minSum)
            minSum = min(num, temp, num * minSum)

            res = max(res, maxSum)

        return res

        # res = [-2, 3, -4]
        # maxSum = [-2, 3, 24]
        # minSum = [-2, -6, ]