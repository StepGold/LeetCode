class Solution:
    def myAtoi(self, s: str) -> int:
        n = 0
        zn = 1
        if not s:
            return 0
        while s and s[0] == ' ':
            s = s[1:]
        if s and s[0] == '+':
            zn = 1
            s = s[1:]
        elif s and s[0] == '-':
            zn = -1
            s = s[1:]

        l = len(s)        
        i = 0
        while (i < l) and (ord(s[i]) < 58) and (ord(s[i]) > 47):
            n += ord(s[i]) - 48
            n *= 10
            i += 1

        n //= 10

        if n > 2 ** 31 - 1:
            if zn == 1:
                return 2**31 - 1
            else:
                return -1 * 2 ** 31
        
        return n * zn
        