# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(root):
            if root.left:
                l = bal(root.left)
            else: l = 0

            if root.right:
                r = bal(root.right)
            else: r = 0

            if (l == -1) or (r == -1) or (abs(l - r) > 1):
                return -1
            else:
                return max(l, r) + 1

        if root:    
            return bal(root) != -1
        else:
            return True