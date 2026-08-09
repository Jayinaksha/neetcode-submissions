class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memory = {}
        ans = []
        for num in nums:
            memory[num] = memory.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in memory.items():
            buckets[freq].append(num)
        ans = []
        for i  in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans