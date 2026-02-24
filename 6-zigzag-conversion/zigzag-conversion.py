class Solution:
    def convert(self, s: str, k: int) -> str:
        n = len(s)
        li = [[] for _ in range(k)]
        i = 0
        buf = 0
        con = k-2
        while i < n:
            if buf < k:
                li[buf].append(s[i])
                buf += 1
            elif con > 0:
                li[con].append(s[i])
                con -= 1
            else:
                buf = 0
                con = k-2
                i -= 1
            i += 1
        

        r = ""
        for i in li:
            for j in i:
                r += j
        return r