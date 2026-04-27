class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        * output should not contain any duplicate triplets
            we may need to store this in a set?
            [1,-1,2,1] (edge case I'd have to look into)
            store each in a set and skip if we have already seen this element
        """
        sorted_nums = sorted(nums)
        res = []

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            calculated_pairs = self.twoSum(sorted_nums, i + 1, sorted_nums[i])
            
            for pair in calculated_pairs:
                res.append(pair)

        return res
    
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        # I need it to give me the target
        res = []
        l = start
        r = len(nums) - 1

        while l < r:
            total = nums[l] + nums[r] + target

            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                res.append((nums[l], nums[r], target))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
        
        return res

        # for i in range(start, len(nums)):
        #     # figure out the remainder number that gives target
        #     # if target - nums[i] in conjugates, add to the res
        #     conjugate = - target - nums[i]

        #     if conjugate in conjugates:
        #         res.append((target, conjugate, nums[i]))
        #     else:
        #         conjugates.add(nums[i]) # we can probably put this in a set?
        
        # return res




