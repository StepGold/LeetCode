class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:


        li = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 39])
        r = 0
        for i in range(left, right + 1):
            n = sum(map(int, bin(i)[2:]))
            r += n in li
        
        return r
