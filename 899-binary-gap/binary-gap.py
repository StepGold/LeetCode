class Solution:
    def binaryGap(self, n: int) -> int:
        r = 0
        s = bin(n)[2:]
        st = -1
        for i in range(len(s)):
            if s[i] == '1':
                if st != -1:
                    r = max(r, i - st)
                st = i
        
        return r