class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        r = []
        for i in range(2 ** 10):
            if list(bin(i)[2:]).count('1') == turnedOn:
                m = i & (2 ** 6 - 1)
                h = i >> 6
                if h < 12 and m < 60:
                    s = str(h) + ':' + '0'*(2 - len(str(m))) + str(m)
                    r.append(s)
        
        return r