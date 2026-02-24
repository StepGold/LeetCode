class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        zn = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            n += x%10
            n *= 10
            x //= 10
        n //= 10
        if n > 2 ** 31:
            return 0
        return n * zn