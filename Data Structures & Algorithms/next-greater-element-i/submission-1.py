class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Keywords
        1. first greater element (strictly increasing)
        2. unique elements in nums 2
        3. if no next greater element, answer is -1
        4. nums1 is a subset of nums2
            nums1[i] == nums2[j] 

        Questions 
        1. looping through nums1 and then determining the next greater from the nums2
        2. there is not always going to be an answer 
        3. number cannot be negative and number are unique

        Thought process
        1. Brute Force: for each char in nums1
            - initiate result array
            - find the index of the char in nums2
            - starting from that char, loop through nums 2 to find the next greater 
            - if found, add result to an array

            Runtime and Space 
            1. time | O(m * n) - m is length of nums1 and n is length of nums2
            2. space | O(m)
        2. Optimized: 
            - get next greater element from looping through nums2
            - create a hash map for nums1 | { num: index }
            - create a result array = [-1,-1,-1] 
            - if top in hash_map
            - calculate difference in days
            - return result
        '''
        hash_map = {}
        stack = []
        res = [-1] * len(nums1)

        for index, char in enumerate(nums1):
            hash_map[char] = index
        
        for index, char in enumerate(nums2):
            while stack and nums2[stack[-1]] < char:
                top = nums2[stack.pop()]
                if top in hash_map:
                    res[hash_map[top]] = char

            stack.append(index)

        return res

            
        
        
        
