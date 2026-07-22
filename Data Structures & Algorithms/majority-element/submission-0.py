from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Questions 
        1. majority element always exist in the array 
        2. floor division

        Thought process 
        1. keep count of elements 
        2. loop through elements dictionary and get the item with the largest count
        3. return item

        Time and space 
        time - O(n)
        space - O(n)
        '''
        res = (0, 0) 

        freq = Counter(nums)

        for key, count in freq.items():
            if count > res[1]:
                res = (key, count)

        return res[0]
        