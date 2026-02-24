class Solution:
    def maxArea(self, h: List[int]) -> int:
        i = 0
        j = len(h) - 1
        r = 0

        while i < j:
            r = max(r, (j - i)*min(h[i], h[j]))
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1

        return r