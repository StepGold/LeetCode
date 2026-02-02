class Solution:
    def isPalindrome(self, x: int) -> bool:
        li = str(x)
        return all([li[i] == li[-(i+1)] for i in range(len(li)//2)])
        