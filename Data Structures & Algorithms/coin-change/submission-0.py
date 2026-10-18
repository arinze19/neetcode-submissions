class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Keywords 
        1. fewest number of coins to make up target amount

        Thought Process 
        1. backtracking [done]
        2. dp
            - sort
            - analyse from the back
            - set

        Questions
        1. can only use coin once? No
        2. sort the coins to avoid unecessary counting
        '''
        cache = set(coins)

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0 # base case 

        for i in range(min(coins), len(dp)):
            # if item in cache 
            if i in cache:
                dp[i] = 1
                continue

            for coin in coins:
                # break loop if coin gets larger than i to prevent back seeks
                if coin > i:
                    break 
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return -1 if dp[amount] == float('inf') else dp[amount]

       


        