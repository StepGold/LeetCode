class Solution:
    def longestBalanced(self, s: str) -> int:
        r = 0
        n =len(s)
        d1 = {}

        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        d2 = {}

        for i in range(n):
            if i > n - r:
                break
            
            d2 = d1.copy()

            for j in range(n-1, i-1, -1):
                if j < i + r:
                    break
                
                ss = set(d2.values())
                if len(ss) == 1 or ((len(ss) == 2) and (0 in ss)):
                    r = max(r, j - i + 1)
                    break
                
                d2[s[j]] -= 1
            
            d1[s[i]] -= 1
        return r