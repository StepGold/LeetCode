class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int("".join(map(lambda x: str(1 - int(x)), bin(n)[2:])), 2)