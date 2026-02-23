class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pol(i, j):
            l = i
            r = j

            while l-1 >= 0 and r+1 < len(s) and s[r+1] == s[l-1]:
                r += 1
                l -= 1

            return l, r


        res = [0, 0]
        dist = 0

        for i in range(len(s)):
            l1, r1 = pol(i, i)
            if dist < r1 - l1 + 1:
                dist = r1 - l1 + 1
                res = [l1, r1]

            if i < len(s) - 1 and s[i] == s[i+1]:
                l2, r2 = pol(i, i+1)
                if dist < r2 - l2 + 1:
                    dist = r2 - l2 + 1
                    res = [l2, r2]
        
        return s[res[0]:res[1]+1]
        