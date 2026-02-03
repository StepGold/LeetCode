class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        p = 0
        while p + 1 < n and nums[p] < nums[p + 1]:
            p += 1
        q = p
        while q + 1 < n and nums[q] > nums[q + 1]:
            q += 1
        r = q
        while r + 1 < n and nums[r] < nums[r + 1]:
            r += 1
        return p > 0 and q > p and q < n - 1 and r == n - 1


