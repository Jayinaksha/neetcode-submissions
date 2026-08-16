class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        pref = collections.deque()
        sufx = collections.deque()
        prefix = [0] * len(height)
        sufix = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                pref.append(0)
            elif height[i-1] > pref[-1]:
                pref.append(height[i-1])
            prefix[i] = pref[-1]
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                sufx.append(0)
            elif height[i+1] > sufx[-1]:
                sufx.append(max(sufx[-1],height[i+1]))
            sufix[i] = sufx[-1]  

        for i in range(len(height)):
            if prefix[i] > height[i] and sufix[i] > height[i]:
                water += (min(prefix[i], sufix[i]) - height[i])
        return water