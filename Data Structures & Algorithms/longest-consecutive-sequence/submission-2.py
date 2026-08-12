class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = set(nums)
        longest = 0
        
        for num in nums:
            if num-1 not in mem:
                current = num
                streak = 1
                while current+1 in mem:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        return longest