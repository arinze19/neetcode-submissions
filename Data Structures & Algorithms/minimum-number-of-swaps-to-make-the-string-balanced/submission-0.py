class Solution:
    def minSwaps(self, s: str) -> int:
        '''
        min number of swaps to make s valid
        - AB [][]
        - [C] [[]]
        - is empty

        Questions 
        1. will it always be possible to swap? No
        '''
        count = 0
        max_count = 0
        for c in s:
            if c == "]":
                count += 1
                max_count = max(count, max_count)
            else:
                count -= 1

        return (max_count + 1) // 2
