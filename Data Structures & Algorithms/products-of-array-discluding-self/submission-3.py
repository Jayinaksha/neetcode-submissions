class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        memory = [1] * len(nums)
        sufx = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                memory[i] = 1
            else:
                memory[i] = nums[i-1]*memory[i-1]
        for i in range(len(nums)-1, -1 , -1):
            if i == len(nums)-1:
                sufx[i] = 1
            else:
                sufx[i] = nums[i+1]*sufx[i+1]
        for i in range(len(nums)):
            ans.append(memory[i] * sufx[i])
        return ans
            