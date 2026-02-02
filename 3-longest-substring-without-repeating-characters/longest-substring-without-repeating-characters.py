class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0 if s == "" else 1
        n = len(s)
        i, j = 0, 1

        while (i < n - r) and (j < n):
            if (len(set(s[i:j])) == j - i):
                r = max(r, j - i)
                j += 1
            else:
                i += 1

        if (len(set(s[i:j])) == j - i):
            r = max(r, j - i)
        
        return r