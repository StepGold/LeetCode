class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        first = n & 1
        n = n >> 1
        second = n & 1
        n = n >> 1
        if first == second:
            return False
        
        a = [first, second]
        ind = 0
        while n > 0:
            if (n & 1 != a[ind]):
                return False
            ind = (ind + 1) % 2
            n = n >> 1
        
        return True