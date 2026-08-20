class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink = 1
        maxk = max(piles)
        prevk = 0
        while mink<=maxk:
            k = int((mink+maxk)/2)
            val = 0
            for pile in piles:
                val += (pile//k) + (1 if (pile%k) else 0)
            if val>h:
                mink = k+1
            elif val<=h:
                prevk = k
                maxk = k-1
        return prevk
