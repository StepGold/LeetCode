class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ss = set()
        for i in range(len(s) - k + 1):
            ss.add(s[i:i+k])
        for i in range(2 ** k, 2 ** (k+1)):
            n = bin(i)[3:]
            if n not in ss:
                return False
        return True