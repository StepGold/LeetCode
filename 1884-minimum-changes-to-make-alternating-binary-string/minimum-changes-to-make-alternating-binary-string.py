class Solution:
    def minOperations(self, s: str) -> int:
        cur = 1
        res1 = 0
        for i in range(len(s)):
            if int(s[i]) == cur:
                res1 += 1
            cur = 1 - cur
        
        cur = 0
        res2 = 0
        for i in range(len(s)):
            if int(s[i]) == cur:
                res2 += 1
            cur = 1 - cur
        return min(res1, res2)