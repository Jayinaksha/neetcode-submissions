import asyncio
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = collections.deque()
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                start = stack[-1][0]
                height = stack[-1][1]
                maxarea = max(maxarea, height * (i - start))
                stack.pop()
            stack.append((start ,h))
        
        for i, h in stack:
            maxarea = max(maxarea,h * (len(heights) - i))
        return maxarea