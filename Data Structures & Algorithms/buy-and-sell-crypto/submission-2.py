class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        KEYWORDS
        
        QUESTIONS 
        1. prices cannot empty? Yes 
        2. if no suitable sell date is available, keep stock and return 0
        
        THOUGHT PROCESS
        1. monotonically increasing stack 
            - if stack length <= 1? return 0 (We can buy stock but can't find a suitable day to sell)
            - stack[-1] - stack[0]? gives us the maximum price and minimum price at a go
        '''
        stack = []
        res = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])

        return res

