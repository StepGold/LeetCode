class Solution:
    def reverse(self, x: int) -> int:
        zn = 1
        if x:
            zn = x // abs(x)
        s = str(abs(x))
        n = int(s[::-1])
        if n > 2**31:
            return 0
        return n * zn