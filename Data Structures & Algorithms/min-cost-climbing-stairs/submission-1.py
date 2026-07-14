class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        backtracking??
        n = 
        '''
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


        

            
