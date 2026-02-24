# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur, r):
            cur = (cur << 1) + root.val
            if not(root.left or root.right):
                r += cur
            if root.left:
                r = dfs(root.left, cur, r)
            if root.right:
                r = dfs(root.right, cur, r)
            return r
        
        r = dfs(root, 0, 0)
        return r
