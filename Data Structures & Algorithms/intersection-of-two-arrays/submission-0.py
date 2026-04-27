class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # is the array sorted? 
        # can the array be None
        res = set()
        cache = set(nums1)

        for i in range(len(nums2)):
            if nums2[i] in cache:
                res.add(nums2[i])
        
        return list(res)