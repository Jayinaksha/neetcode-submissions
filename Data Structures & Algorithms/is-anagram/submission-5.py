class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = []
        hash2 = []
        for S in s:
            hash.append(S)
        for T in t:
            hash2.append(T)
        if collections.Counter(hash) == collections.Counter(hash2):
            return True
        return False