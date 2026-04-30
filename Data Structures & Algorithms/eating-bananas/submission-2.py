import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # runtime 
        # O(n) + O(log(highest)) * O(n) = O(n * log(highest))

        # space
        # O(1)
        min_rate = float("inf")
        min_hours = 0
        highest = max(piles) # O(len(piles) or O(n))

        left = 1
        right = highest

        while left <= right: # O(log(highest))
            rate = (left + right) // 2

            # accumulate total hours for each pile 
            hours = 0 

            for pile in piles: # O(n)
                hours += math.ceil(pile / rate)
            
            # if rate less than min_rate and hours <= 
            if rate < min_rate and hours <= h:
                min_rate = rate
                min_hours = hours

            # if rate exceeds current h; move to the left, else move to the right
            if hours > h:
                left = rate + 1
            else:
                right = rate - 1

        return min_rate
