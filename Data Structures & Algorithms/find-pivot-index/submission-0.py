class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = nums[i] + prefix_sum[i]

        # [0,3,5,6]
        # right = prefix_sum[n] - prefix_sum[i + 1]
        # left = prefix_sum[i]
        for i in range(n):
            right = prefix_sum[n] - prefix_sum[i + 1]
            left = prefix_sum[i]

            if right == left:
                return i

        return -1