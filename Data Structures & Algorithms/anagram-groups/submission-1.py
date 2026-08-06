class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = collections.defaultdict(list)
        for word in strs:
          memory[str(sorted(word))].append(word)
        return list(memory.values())