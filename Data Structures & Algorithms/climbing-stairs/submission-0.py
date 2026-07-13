class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Backtracking -> Top-Down (Memoization) -> Bottom-Up (Tabulation)
        count = 0
        memo = defaultdict(int)

        def backtrack(i):
            nonlocal count 

            if i in memo:
                return memo[i]

            # base case 
            if i == n:
                memo[i] += 1
                return memo[i]

            # bad case
            if i > n:
                return 0

            # choices
            memo[i] = backtrack(i + 1) + backtrack(i + 2)

            return memo[i]

        return backtrack(0)
        '''

        dp = [0] * (n + 1) 
        # why do we make n + 1 array? 
        # i guess we are using this to make the array more human readable

        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]





