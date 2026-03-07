class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        st = s + s
        tup = '0', '1'

        d1 = 0
        d2 = 0
        res = n

        for i in range(2*n):
            ind = int(i & 1)
            s1 = tup[ind]
            s2 = tup[1 - ind]
            
            if st[i] != s1:
                d1 += 1
            else:
                d2 += 1
            
            if i > n - 1:
                prev_ind = int((i - n) & 1)
                prev1 = tup[prev_ind]
                prev2 = tup[1 - prev_ind]

                if st[i - n] != prev1:
                    d1 -= 1
                else:
                    d2 -= 1
            
            if i >= n - 1:
                res = min(res, d1, d2)
        
        return res