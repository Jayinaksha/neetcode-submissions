class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        idx = 0 
        idx_rev = len(heights)-1
        while idx <= idx_rev:
            area = (idx_rev - idx) * min(heights[idx], heights[idx_rev])
            if heights[idx] < heights[idx_rev]:
                idx += 1
            elif heights[idx] > heights[idx_rev]:
                idx_rev -= 1
            else:
                idx += 1
                idx_rev -= 1
            maxarea = max(maxarea, area)
        
        return maxarea