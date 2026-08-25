class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # loop through the heights 
        # keep a monotonically increasing stack  - identifies the max range we can extend the bottom element of the stack
        # once we come across an item that is lower we can start to answer the questions on the stack
        # 
        stack = [] # (start_index, height)
        max_area = 0
        n = len(heights)

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                top_index, top_height = stack.pop() # get the items at the top
                start = top_index # shifting our start value back to account for gaps in the stack
                max_area = max(max_area, top_height * (index - top_index))

            stack.append((start, height))

        # account for indexes still on the stack
        for index, height in stack:
            max_area = max(max_area, height * (n - index))

        return max_area

