class Solution:
    def minRemoval(self, li: List[int], k: int) -> int:
        li.sort()
        n = len(li)
        r = n
        i = 0
        j = 0
        while j < n:
            while (i < n) and (li[i] <= k*li[j]):
                i += 1
            r = min(r, n - (i - j))
            j += 1

        return r

    