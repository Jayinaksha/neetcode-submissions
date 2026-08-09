class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            s = 'EMPTY'
            return s
        s = ",#".join(strs)
        return s
    def decode(self, s: str) -> List[str]:
        if s == 'EMPTY':
            return []
        strs = [item.strip("") for item in s.split(",#")]
        return strs
