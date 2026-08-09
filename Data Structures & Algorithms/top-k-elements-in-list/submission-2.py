class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memory = {}
        ans = []
        for num in nums:
            memory[num] = memory.get(num, 0) + 1
        sorted_nums = sorted(memory.keys(), key=lambda x: memory[x], reverse=True)
        return sorted_nums[:k]