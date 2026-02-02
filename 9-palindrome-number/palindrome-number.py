class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        i = 1
        while i <= x:
            y = y*10 + ((x % (i * 10)) // i)
            i *= 10
        return x - y == 0
        