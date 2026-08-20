class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 1001
        for num in nums:
            if num < min:
                min = num
        return min