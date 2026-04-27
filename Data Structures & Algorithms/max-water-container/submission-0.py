class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Your code goes here
        left = 0
        right = len(heights) - 1
        res = float("-inf")

        while left < right:
            # get the smallest height of the two [h = height]
            height = min(heights[left], heights[right])

            # get the distance between both (w = right - left) [width]
            width = right - left

            # update the largest area (res = max(h * w, res))
            res = max(height * width, res)

            # if heights[left] < heights[right]: left += 1
            if heights[left] < heights[right]:
                left += 1
            # otherwise: right -= 1
            else:
                right -= 1
                
        return res