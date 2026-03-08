class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = ''
        d = {'0': '1', '1': '0'}
        for i in range(len(nums)):
            s += d[nums[i][i]]
        
        return s
