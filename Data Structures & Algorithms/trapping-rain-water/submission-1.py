class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        highest = 0
        left = [0 * i for i in range(len(height))]
        right = [0 * i for i in range(len(height))]
        # build max from left to right
        for i in range(len(height)):
            left[i] = max(highest, height[i])
            highest = left[i]

        highest = 0

        for j in range(len(height) - 1, -1, -1):
            right[j] = max(highest, height[j])
            highest = right[j]

        
        for k in range(len(height)):
            mini = min(left[k], right[k])
            count += mini - height[k]

        return count


