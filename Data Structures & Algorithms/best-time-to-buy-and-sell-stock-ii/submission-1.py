class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        KEYWORDS
        1. buy and sell on same day (dp)
        2. can hold at most one share of stock at any time 

        QUESTIONS 
        1. price list can be empty? No
        2. what is result when price list length is one? 0

        THOUGHT PROCESS
        1. prefix sum/dp
        2. monotonic stack?

        BRUTE FORCE
            - backtracking (find the most optimal combination)
        OPTIMIAL
            - bottom up

        # we can holddd
        '''
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]

        return res
        


        