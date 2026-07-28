class NumArray:

    def __init__(self, nums: List[int]):
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        self.prefix = prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

    # [0,2] - -2
    # [2,5] - 
    # [0,5]
    # [0,-2,-2,1,-4,-2,-3]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)