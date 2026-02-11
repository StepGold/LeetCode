class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(min([len(j) for j in strs]) + 1):
            if not(all([(strs[0][:i] in strs[j][:i]) for j in range(len(strs))])):
                return strs[0][:i-1]
        return strs[0][:i]