class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = []
        for i, v in enumerate(nums):
            r.append(nums[(i + v) % n])
        return r