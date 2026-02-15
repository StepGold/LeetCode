class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(i) for i in a[::-1]]
        b = [int(i) for i in b[::-1]]
        c = []
        prev = 0
        while a or b:
            cur = 0
            if a:
                cur += a[0]
                a.pop(0)
            if b:
                cur += b[0]
                b.pop(0)
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