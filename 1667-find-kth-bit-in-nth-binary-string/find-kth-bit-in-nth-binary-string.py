class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(n-1):
            li = [str(1 - int(i)) for i in s]
            st = "".join(li[::-1])
            s = s + '1' + st
        print(s)
        return s[k-1]