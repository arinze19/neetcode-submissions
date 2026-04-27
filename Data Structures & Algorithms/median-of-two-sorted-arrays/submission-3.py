import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        concatenate both arrays and then take the midpoint
        - get the length of both values 
        - using the length we can determine the lenght of the combined 
        - 
        """
        i = 0
        j = 0
        total = []

        # calculate and arrange the arrays until all empty
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                total.append(nums1[i])
                i += 1
            else:
                total.append(nums2[j])
                j += 1

        if i < len(nums1):
            total += nums1[i:]
        
        if j < len(nums2):
            total += nums2[j:]

        mid = len(total) // 2

        if len(total) % 2 == 0:
            return (total[mid] + total[mid - 1]) / 2
        else:
            return total[mid]