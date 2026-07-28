from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        count = 0
        prefix_count = defaultdict(int)

        prefix_count[0] = 1

        for num in nums:
            sum_ += num # add current number to sum
            target = sum_ - k

            if target in prefix_count:
                count += prefix_count[target]

            prefix_count[sum_] += 1

        return count

