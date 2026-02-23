class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pol(s: str):
            return s[:len(s)//2] == s[:(len(s) + 1)//2 - 1:-1]
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                if pol(s[j: j+i]):
                    return s[j: j+i]
        