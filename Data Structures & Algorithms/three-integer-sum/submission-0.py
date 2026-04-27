class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        * output should not contain any duplicate triplets
            we may need to store this in a set?
            [1,-1,2,1] (edge case I'd have to look into)
            store each in a set and skip if we have already seen this element
        """
        sorted_nums = sorted(nums)
        res = set()

        for i in range(len(sorted_nums)):
            calculated_pairs = self.twoSum(sorted_nums, i + 1, sorted_nums[i])
            
            if calculated_pairs:
                for calculated_pair in calculated_pairs:
                    res.add(calculated_pair)


        return list(res)
    
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        # I need it to give me the target
        res = []
        conjugates = set()

        for i in range(start, len(nums)):
            # figure out the remainder number that gives target
            # if target - nums[i] in conjugates, add to the res
            conjugate = - target - nums[i]

            if conjugate in conjugates:
                res.append((target, conjugate, nums[i]))
            else:
                conjugates.add(nums[i]) # we can probably put this in a set?
        
        return res




