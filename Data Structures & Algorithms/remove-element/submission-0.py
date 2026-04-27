class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # loop through the nums
        # inititate a trailing pointer j that tracks the position of current val
        # once we encounter an item that is not val, we swap

        """ 
        j = 0
        i = 0

        i = 1 | i == val
        i = 2 | i != val | [2,1,1,3,4] | j = 1
        i = 3 | i != val | [2,3,1,1,4] | j = 2
        """
        nextVal = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[nextVal] = nums[nextVal], nums[i]
                nextVal += 1
        
        return len(nums[:nextVal])
