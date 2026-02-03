class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        r = 1
        n = len(s)
        i, j = 0, 1

        st = set(s)
        d = dict()

        for k in st:
            d[k] = 0

        d[s[0]] = 1

        while (i < n - r) and (j < n):
            if (d[s[j]] == 0):
                r = max(r, j - i + 1)
                d[s[j]] += 1
                j += 1
            else:
                d[s[i]] -=1
                i += 1

        if (len(set(s[i:j])) == j - i):
            r = max(r, j - i)
        
        return r