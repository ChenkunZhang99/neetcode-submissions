class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                popped = stack.pop()
                height = heights[popped]
                right = i
                left = stack[-1] if stack else -1
                max_area = max(max_area, height * (right - left - 1))
            stack.append(i)

        while stack:
            popped = stack.pop()
            height = heights[popped]
            right = n
            left = stack[-1] if stack else -1
            max_area = max(max_area, height * (right - left - 1))

        return max_area       