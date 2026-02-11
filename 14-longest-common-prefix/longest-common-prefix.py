class Solution:
    def longestCommonPrefix(self, li: List[str]) -> str:
        r = ""
        li.sort()
        first=li[0]
        last=li[-1]

        for i in range(min(len(first), len(last))):
            if(first[i]!=last[i]):
                return r
            r += first[i]
        return r 