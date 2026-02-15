class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(i) for i in a]
        b = [int(i) for i in b]
        c = []
        prev = 0
        aa = len(a)
        bb = len(b)
        while aa or bb:
            cur = 0
            if aa:
                cur += a[aa - 1]
                aa -= 1
            if bb:
                cur += b[bb - 1]
                bb -= 1
            cur += prev
            prev = cur // 2
            cur %= 2

            c.append(cur)
        
        if prev:
            c.append(prev)
        
        s = ""
        for i in c[::-1]:
            s += str(i)
        
        return s
