class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        we can initiate two pointers
        total = nums[i] + nums[j]
        if total == target:
            return [i + 1, j + 1]
        elif total < target:
            i += 1
        else:
            j -= 1
        """
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]

            if total == target:
                return [i + 1, j + 1]
            elif total < target:
                i += 1
            else: 
                j -= 1
        
        