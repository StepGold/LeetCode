class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = s.count('a')
        b = 0
        r = a + b
        for i in s:
            if i == 'b':
                b += 1
            else:
                a -= 1
            r = min(r, a+b)
        return r