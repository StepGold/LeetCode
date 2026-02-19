class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        r = 0
        li = [0, 0]
        li[int(s[0])] += 1

        print(li, end=' ')
        print(r)

        cur = s[0]
        for i in s[1:]:
            if i == cur:
                li[int(i)] += 1
            else:
                r += min(li)
                li[int(i)] = 1
                cur = i
            
            print(li, end=' ')
            print(r)

        r += min(li)
        
        return r