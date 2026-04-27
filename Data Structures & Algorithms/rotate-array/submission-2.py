class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        k is non-negative 
        slow and fast pointer?
        loop until k
        swap

        - create a new array with 0 values 
        - loop through each item in nums and add to newly created array

        """
        cache = [0] * len(nums)
        n = len(nums)

        for i in range(len(nums)):
            index = (i + k) % n
            cache[index] = nums[i]

        for i in range(len(cache)):
            nums[i] = cache[i]
            