class Solution:
    def minPartitions(self, n: str) -> int:
        m = 0
        for i in n:
            x = int(i)
            if x > m:
                m = x
                if m == 9:
                    return 9
        return m