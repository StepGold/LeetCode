class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        m = max(arr)
        arr.sort()
        r = 0
        i = 0
        while 2**i < m:
            i += 1
        li = [[] for _ in range(i+1)]
        masks = [1 << j for j in range(i+1)]
        
        for i in arr:
            r = 0
            for j in masks:
                if i & j:
                    r += 1
            li[r].append(i)

        r = []
        for i in li:
            r+= i
        return r