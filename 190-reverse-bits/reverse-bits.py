class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)[2:]
        s = '0'*(32 - len(a)) + a
        return int(s[::-1], 2)
