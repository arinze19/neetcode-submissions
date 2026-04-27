class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort people array
        # infinite number of boats 
        # sliding window
        # two pointers 
        # try to pair the least and most elements
        # [[1,2],3,5]
        # [1,2,2,3,3] | 3
        count = 0
        n = len(people)
        left = 0
        right = n - 1

        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            count += 1
            right -= 1

        return count

        
            
