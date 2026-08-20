class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = sorted(nums)
        return n[0]