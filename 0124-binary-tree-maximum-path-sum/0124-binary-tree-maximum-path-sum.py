# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
    
        m = float('-inf')

        def findMax(root):
            nonlocal m
    
            if root == None: 
                return 0

            l = max(0,findMax(root.left))
            r = max(0,findMax(root.right))

            m = max(m, l+r+root.val)

            return root.val + max(l,r)
 
        findMax(root)
        return m