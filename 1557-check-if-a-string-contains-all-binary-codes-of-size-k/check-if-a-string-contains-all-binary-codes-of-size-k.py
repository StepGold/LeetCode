class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ss = set()
        l = 2**k - 1
        n = 2**k
        for i in range(len(s) - k + 1):
            ss.add(s[i:i+k])
            if len(ss) == n:
                return True
        return False