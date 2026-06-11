from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # BRUTE FORCE 
        # loop through arr (i)
        # loop though arr (j = i + 1)
        # compare
        # runtime | O(n^2)
        # space | O(1)

        # OPTIMIZED 
        # time | O(n)
        # space | O(n)

        # Questions 
        # are there only two indices that satisfy this requirement?? Yes
        cache = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in cache and abs(cache[nums[i]][-1] - i) <= k:
                return True

            cache[nums[i]].append(i)

        return False
