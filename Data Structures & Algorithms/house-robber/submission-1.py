class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Questions 
        1. minimum length of 1 house? Yes 
        2. do we have to jump by only 2? No
        
        Thought process
        1. backtrack (skip/take)
        2. cannot rob adjacent houses? (jump by at least 2)

        [1,2]
        {
          0: 1,
          1: 2 # this identifies the max number of items we can reach starting from this point
        }

        bottom-up
        '''

        '''
        n = len(nums)
        memo = {}
        
        def backtrack(i):
            # base case 
            if i >= n:
                # memo[i] = max(res, total)
                return 0

            # choices 
            # take current choice 
            memo[i] = max(nums[i] + backtrack(i + 2), backtrack(i + 1))

            return memo[i]

        return backtrack(0)
        '''

        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]