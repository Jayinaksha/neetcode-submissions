class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            s = 'EMPTY'
            return s
        s = "".join(stri + ",#" for stri in strs)
        return s
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strs = s.split(",#")[:-1]
        return strs
