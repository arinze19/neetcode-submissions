class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            if height[left] < height[right]:
                res += min(maxLeft, maxRight) - height[left]
                left += 1
                maxLeft = max(height[left], maxLeft)
            else:
                res += min(maxRight, maxLeft) - height[right]
                right -= 1
                maxRight = max(height[right], maxRight)

        return res 

