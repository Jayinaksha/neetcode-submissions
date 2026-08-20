class Solution:
    def findMin(self, nums: List[int]) -> int:
        maxa = len(nums)-1
        mina = 0
        while mina<maxa:
            mid = int((mina+maxa)/2)
            if nums[mid] > nums[maxa]:
                mina = mid+1
            else:
                maxa = mid
        return nums[mina]
