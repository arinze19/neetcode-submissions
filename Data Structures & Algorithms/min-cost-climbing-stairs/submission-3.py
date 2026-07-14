class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        backtracking??
        n = 
        n = len(cost)
        res = float("inf")
        memo = {}

        def backtrack(i):
            if i in memo:
                return memo[i]

            # base case 
            if i >= n:
                memo[i] = 0
                return memo[i]

            # move by one
            memo[i] = cost[i] + min(backtrack(i + 1), backtrack(i + 2))

            return memo[i]

        return min(backtrack(0), backtrack(1))
        '''

        '''
        [1,2,3]      [1,2,3]
        [0,0,0,0] -> [0,0,1,0]
            min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        NOTES:
        1. to get to target step, there is no cost attached 
        '''

        '''
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]
        '''

        prev = 0 # i - 2
        curr = 0 # i - 1

        for i in range(2, len(cost) + 1):
            temp = curr
            curr = min(cost[i - 1] + curr, cost[i - 2] + prev)
            prev = temp

        return curr




        

            
