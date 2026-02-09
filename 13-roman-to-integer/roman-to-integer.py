class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        while s and s[0]=='M':
            s = s[1:]
            n+=1000
        if "CM" in s:
            n+=900
            s=s[2:]
        elif s and s[0] == 'D':
            n+=500
            s = s[1:]
        elif "CD" in s:
            n+=400
            s = s[2:]

        while s and s[0]=='C':
            s = s[1:]
            n+=100
        if "XC" in s:
            n+=90
            s=s[2:]
        elif s and s[0] == 'L':
            n+=50
            s = s[1:]
        elif "XL" in s:
            n+=40
            s = s[2:]

        while s and s[0]=='X':
            s = s[1:]
            n+=10
        if "IX" in s:
            n+=9
            s=s[2:]
        elif s and s[0] == 'V':
            n+=5
            s = s[1:]
        elif "IV" in s:
            n+=4
            s = s[2:]

        while s and s[0]=='I':
            s = s[1:]
            n+=1

        return n
        
        