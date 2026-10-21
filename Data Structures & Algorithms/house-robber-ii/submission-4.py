class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case 
        if len(nums) == 1:
            return nums[0]

        def solve(i, memo):
            if i == len(nums):
                return 0

            # overshoot 
            if i > len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + solve(i + 2, memo), solve(i + 1, memo))

            return memo[i]

        def solve2(i, memo):
            if i == (len(nums) - 1):
                return 0

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + solve2(i + 2, memo), solve2(i + 1, memo))

            return memo[i]

        return max(solve2(0, {}), solve(1, {}))

