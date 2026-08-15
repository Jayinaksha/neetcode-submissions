class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for i, num in enumerate(nums):
            idx = 0
            idx_rev = len(nums) -1
            while idx < idx_rev :
                if idx == i:
                    idx +=1
                    continue
                if idx_rev == i:
                    idx_rev -= 1
                    continue
                if (num +  nums[idx] + nums[idx_rev]) == 0:
                    answer.add(tuple(sorted((num, nums[idx], nums[idx_rev]))))
                    idx +=1
                    idx_rev-=1
                elif (num +  nums[idx] + nums[idx_rev] > 0):
                    idx_rev -= 1
                elif (num +  nums[idx] + nums[idx_rev] < 0):
                    idx += 1
        return [list(ans) for ans in answer]
