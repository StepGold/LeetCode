class Solution:
    def longestBalanced(self, s: str) -> int:
        def mono(s):
            r = 1
            ch = s[0]
            cur = 0
            for i in s:
                if i == ch:
                    cur += 1
                else:
                    r = max(r, cur)
                    ch = i
                    cur = 1
            r = max(r, cur)
            return r
        

        def duos(s, c1, c2):
            r = 0
            balance = 0
            d = {0: -1}
            for i in range(len(s)):
                if s[i] == c1:
                    balance += 1
                else:
                    balance -= 1

                if balance in d:
                    r = max(r, i - d[balance])
                else:
                    d[balance] = i
            return r

        def duo(s, c1, c2, c3):
            li = s.split(c3)
            r = 0
            for i in li:
                r = max(r, duos(i, c1, c2))
            return r


        def trio(s, c1, c2, c3):
            d = {(0, 0) : -1}
            r = 0
            b1, b2 = 0, 0
            for i in range(len(s)):
                if s[i] == c1:
                    b1 += 1
                elif s[i] == c2:
                    b2 += 1
                    b1 -= 1
                else:
                    b2 -= 1
                
                if (b1, b2) in d:
                    r = max(r, i - d[(b1, b2)])
                else:
                    d[(b1, b2)] = i
            return r


        return max(
            mono(s),
            duo(s, 'a', 'b', 'c'),
            duo(s, 'a', 'c', 'b'),
            duo(s, 'b', 'c', 'a'),
            trio(s, 'a', 'b', 'c'),
        )