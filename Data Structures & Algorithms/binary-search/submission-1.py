class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = 0
        idx_rev = len(nums) - 1
        while idx<=idx_rev:
            mid = int((idx+idx_rev)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                idx = mid+1
            elif nums[mid] > target:
                idx_rev = mid-1
        return -1