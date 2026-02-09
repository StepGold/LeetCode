# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        li = []
        def convert(r):
            if r.left:
                convert(r.left)
            li.append(r.val)
            if r.right:
                convert(r.right)
        
        convert(root)

        def create(a, b):
            if a > b:
                return None
            
            m = (a + b) // 2
            left = create(a, m-1)
            right = create(m+1, b)

            r = TreeNode(li[m], left, right)

            return r
        
        return create(0, len(li) - 1)
