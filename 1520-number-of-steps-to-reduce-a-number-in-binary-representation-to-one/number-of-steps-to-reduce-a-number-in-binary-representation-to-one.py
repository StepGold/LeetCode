class Solution:
    def numSteps(self, s: str) -> int:
        k = 0
        while s != "1":
            k += 1
            if s[-1] == '0':
                s = s[:-1]
            else:
                ind = 2
                car = 1
                s = s[:-1] + '0'
                while ind < len(s) + 1:
                    if s[-ind] == '0':
                        s = s[:-ind] + '1' + s[-ind+1:]
                        car = 0
                        break
                    else:
                        s = s[:-ind] + '0' + s[-ind + 1:]
                    ind += 1
                if car == 1:
                    s = '1' + s

        return k
                
