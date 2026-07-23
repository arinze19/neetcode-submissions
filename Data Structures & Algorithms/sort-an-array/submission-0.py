class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        1. deconstruct
        2. merge 

        Thought process 
        1. [1,2]
            - deconstruct([1,2])
            - merge([1], [2])
        '''
        return self.deconstruct(nums)

    def deconstruct(self, arr):
        # base case 
        if len(arr) <= 1:
            return arr

        # split from the mid point and pass into next recursive call
        mid = len(arr) // 2

        res = self.merge(self.deconstruct(arr[:mid]), self.deconstruct(arr[mid:]))

        return res

    def merge(self, arr1, arr2):
        res = []
        left = 0
        right = 0

        while left < len(arr1) and right < len(arr2):
            if arr1[left] < arr2[right]:
                res.append(arr1[left])
                left += 1
            else:
                res.append(arr2[right])
                right += 1
            
        if left < len(arr1):
            res += arr1[left:]

        if right < len(arr2):
            res += arr2[right:]

        return res 