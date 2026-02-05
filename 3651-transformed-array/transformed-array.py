class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = []
        for i in range(n):
            r.append(nums[(i + nums[i]) % n])
        return r