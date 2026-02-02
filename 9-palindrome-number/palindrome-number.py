class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        li = str(x)
        y = int(li[::-1])
        return x - y == 0
        