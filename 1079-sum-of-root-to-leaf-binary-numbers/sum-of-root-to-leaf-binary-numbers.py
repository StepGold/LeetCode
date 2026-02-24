# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur):
            cur = (cur << 1) + root.val
            if not(root.left or root.right):
                self.r += cur
            if root.left:
                dfs(root.left, cur)
            if root.right:
                dfs(root.right, cur)
            return
        
        self.r = 0
        dfs(root, 0)
        return self.r
