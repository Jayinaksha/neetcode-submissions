class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = int((left+right)//2)
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        la = nums[:left]
        ra = nums[left:]

        lla = 0
        rla = len(la)-1
        while lla<=rla:
            mid = int((lla+rla)//2)
            if la[mid] == target:
                return mid
            elif la[mid] > target:
                rla = mid-1
            else:
                lla = mid+1

        lra = 0
        rra = len(ra)-1
        while lra<=rra:
            midr = int((lra+rra)//2)
            if ra[midr] == target:
                return left+midr
            elif ra[midr] > target:
                rra = midr-1
            else:
                lra = midr+1
        return -1